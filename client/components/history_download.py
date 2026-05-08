import streamlit as st



def render_history_download():
    st.sidebar.markdown("---")
    st.sidebar.header("Chat Settings")
    
    api_key_input = st.sidebar.text_input(
        "Groq API Key (Optional)", 
        type="password", 
        value=st.session_state.get("groq_api_key", ""),
        help="Leave blank to use the default built-in API key."
    )
    
    if st.sidebar.button("Set API Key"):
        st.session_state.groq_api_key = api_key_input
        if api_key_input.strip():
            st.sidebar.success("✅ Custom API Key is now being used!")
        else:
            st.sidebar.info("ℹ️ Using default built-in API Key.")
    if st.session_state.get("messages"):
        chat_text="\n\n".join([f"{m['role'].upper()}: {m['content']}" for m in st.session_state.messages])
        st.sidebar.download_button("📥 Download Chat History",chat_text,file_name="chat_history.txt",mime="text/plain")