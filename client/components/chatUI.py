import streamlit as st
from utils.api import ask_question

def render_chat():
    col1, col2 = st.columns([8, 2])
    with col1:
        st.subheader(" Chat with your documents")
    with col2:
        if st.button("🗑️ Clear Chat"):
            st.session_state.messages = []
            st.rerun()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Render existing chat history
    for msg in st.session_state.messages:
        avatar = "🧑‍🎓" if msg["role"] == "user" else "🤖"
        st.chat_message(msg["role"], avatar=avatar).markdown(msg["content"])

    # Quick Prompts
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### ⚡ Quick Actions")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📝 Summarize the document"):
            st.session_state.quick_prompt = "Provide a high-level summary of the document."
    with col2:
        if st.button("🔑 Key concepts"):
            st.session_state.quick_prompt = "What are the key concepts discussed in this document?"
    with col3:
        if st.button("👶 Explain like I'm 5"):
            st.session_state.quick_prompt = "Explain the core concepts of this document like I am 5 years old."

    # Input and response
    user_input = st.chat_input("Type your question here...")
    
    if "quick_prompt" in st.session_state and st.session_state.quick_prompt:
        user_input = st.session_state.quick_prompt
        st.session_state.quick_prompt = None

    if user_input:
        st.chat_message("user", avatar="🧑‍🎓").markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        api_key_to_use = st.session_state.get("groq_api_key", "")
        response = ask_question(user_input, st.session_state.session_id, api_key_to_use)
        if response.status_code == 200:
            data = response.json()
            answer = data["response"]
            sources = data.get("sources", [])
            st.chat_message("assistant", avatar="🤖").markdown(answer)
            if sources:
                st.markdown("📄 **Sources:**")
                for src in sources:
                    st.markdown(f"- `{src}`")
            st.session_state.messages.append({"role": "assistant", "content": answer})
        else:
            st.error(f"Error: {response.text}")