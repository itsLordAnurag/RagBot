import streamlit as st
import base64
from components.upload import render_uploader
from components.history_download import render_history_download
from components.chatUI import render_chat

def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    with open("styles.css") as style_file:
        custom_css = style_file.read()
        
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_string});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        {custom_css}
        </style>
        """,
        unsafe_allow_html=True
    )

import uuid

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

st.set_page_config(page_title="ExamGPT",layout="wide")
set_background("/home/anurag/c codes/python-development/ragbot/ragbot/w1.jpg")

st.title("ExamGPT")


render_uploader()
render_chat()
render_history_download()