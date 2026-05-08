import streamlit as st
import base64
from components.upload import render_uploader
from components.history_download import render_history_download
from components.chatUI import render_chat

import os
import base64

def set_background(image_filename):
    # Dynamically get the folder where app.py is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Safely construct absolute paths for both files
    image_path = os.path.join(current_dir, image_filename)
    css_path = os.path.join(current_dir, "styles.css")

    with open(image_path, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
        
    with open(css_path) as style_file:
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
set_background("w1.jpg")

st.title("ExamGPT")


render_uploader()
render_chat()
render_history_download()