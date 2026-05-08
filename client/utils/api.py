import requests
from config import API_URL


def upload_pdfs_api(files, session_id):
    files_payload=[("files",(f.name,f.read(),"application/pdf")) for f in files]
    return requests.post(f"{API_URL}/upload_pdfs/?session_id={session_id}",files=files_payload)

def ask_question(question, session_id, groq_api_key=""):
    return requests.post(f"{API_URL}/ask/?session_id={session_id}",data={"question":question, "groq_api_key": groq_api_key})

def clear_db_api(session_id):
    return requests.delete(f"{API_URL}/clear_db/?session_id={session_id}")