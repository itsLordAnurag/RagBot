import streamlit as st
from utils.api import upload_pdfs_api, clear_db_api

def render_uploader():
    st.sidebar.header("Upload PDFs")
    uploaded_files=st.sidebar.file_uploader("Upload  multiple PDFs",type="pdf",accept_multiple_files=True)
    
    clear_before = st.sidebar.checkbox("Clear old documents before uploading", value=True)
    
    if st.sidebar.button("Upload to DB") and uploaded_files:
        if clear_before:
            with st.spinner("Clearing old documents..."):
                clear_db_api(st.session_state.session_id)
                
        with st.spinner("Processing new documents..."):
            response=upload_pdfs_api(uploaded_files, st.session_state.session_id)
            if response.status_code==200:
                st.sidebar.success("Uploaded successfully")
            else:
                st.sidebar.error(f"Error: {response.text}")
                
    st.sidebar.markdown("---")
    if st.sidebar.button("🗑️ Clear Database Now"):
        with st.spinner("Clearing database..."):
            res = clear_db_api(st.session_state.session_id)
            if res.status_code == 200:
                st.sidebar.success("Database cleared!")
            else:
                st.sidebar.error("Failed to clear database.")