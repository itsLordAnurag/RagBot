# ExamGPT (RagBot 2.0) 🤖📚

ExamGPT is a modern, responsive Retrieval-Augmented Generation (RAG) chatbot designed to help students and researchers interact with their study materials (PDFs, textbook chapters, lecture notes, etc.). 

It uses **FastAPI** for a fast, concurrent backend API, **Streamlit** for a frontend, **Pinecone** for  vector search, and **Groq (Llama 3)** to answer questions accurately using either documents or general knowledge.

🔗 **Live Link**: [itslordragbot.streamlit.app](https://itslordragbot.streamlit.app/)

---

##  Features

- **Optional API Keys**: Users can enter their own Groq API keys securely in the sidebar to bypass rate limits, falling back to the built in system key if left blank.
- **Modern LCEL Chain**: Utilizes modern LangChain Expression Language (LCEL) chains (`create_retrieval_chain` & `create_stuff_documents_chain`) for robust and clean execution.
- **Quick Actions**: One-click prompt buttons to instantly "Summarize the document", extract "Key concepts", or "Explain like I'm 5".
- **Chat History**: Export your current study session using the "Download Chat History" button.
- **Auto-Cleanup**: Temporary PDF uploads are automatically deleted from the server disk after being successfully embedded and uploaded to Pinecone.

---

## 🛠️ Architecture & Tech Stack

- **Frontend**: Streamlit, custom CSS (`styles.css`).
- **Backend API**: FastAPI (running synchronously in background threadpools to prevent blocking).
- **LLM**: Groq (`llama-3.3-70b-versatile`).
- **Embeddings**: Google Generative AI Embeddings (`gemini-embedding-2`).
- **Vector Database**: Pinecone (Serverless).
- **PDF Loader**: PyPDF via LangChain.

---

## 📂 Project Structure

```text
RagBot/
├── client/                # Streamlit Frontend
│   ├── components/        # Sidebar upload, Chat UI, History download
│   │   ├── chatUI.py
│   │   ├── history_download.py
│   │   └── upload.py
│   ├── utils/
│   │   └── api.py         # Client wrapper for FastAPI requests
│   ├── app.py             # Streamlit entry point
│   ├── config.py          # Frontend environment config
│   └── styles.css         # Glassmorphism design stylesheet
└── server/                # FastAPI Backend
    ├── modules/           # Core LLM, Vectorstore, and Query modules
    │   ├── llm.py
    │   ├── load_vectorstore.py
    │   ├── pdf_handlers.py
    │   └── query_handlers.py
    ├── main.py            # FastAPI entry point
    ├── logger.py          # Logging configuration
    └── requirements.txt   # Backend python packages
```

---

## ⚙️ Local Setup

### Prerequisites
- Python 3.11+
- A Pinecone account (with a serverless index set up)
- API Keys for: **Groq**, **Pinecone**, and **Google GenAI** (for embeddings)

### 1. Clone the repository
```bash
git clone https://github.com/itsLordAnurag/RagBot.git
cd RagBot
```

### 2. Configure Environment Variables
Create a `.env` file inside the `server/` directory:
```env
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_pinecone_index_name
GOOGLE_API_KEY=your_google_gemini_api_key
GROQ_API_KEY=your_groq_api_key
```

### 3. Run Backend (FastAPI)
```bash
cd server
python3 -m venv myenv_server
source myenv_server/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
The backend will run on `http://127.0.0.1:8000`.

### 4. Run Frontend (Streamlit)
```bash
# In a new terminal tab
cd client
python3 -m venv myenv_client
source myenv_client/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
Open your browser to `http://localhost:8501`.

---

## 🌐 Deployment

### Backend (e.g., Render)
1. Deploy `server/` folder as a Python Web Service on Render.
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `uvicorn main:app --host 0.0.0.0 --port 10000`
4. Add all environment variables (`PINECONE_API_KEY`, etc.) in Render's dashboard.

### Frontend (Streamlit Community Cloud)
1. Deploy `client/app.py` directly on Streamlit Cloud.
2. Update `client/config.py` to point `API_URL` to your live Render backend URL before deploying.
