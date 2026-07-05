# 📄 AI Document Search (RAG Chatbot)

An AI-powered PDF Question Answering System built using **Retrieval-Augmented Generation (RAG)**.

Users can upload PDF documents and ask questions in natural language. The application retrieves the most relevant document sections using semantic search and generates accurate answers with Google Gemini.

---

## ✨ Features

- 📄 Upload PDF documents
- 🔍 Extract text automatically
- ✂️ Intelligent text chunking
- 🧠 Semantic embeddings using Hugging Face
- 📚 FAISS vector database
- 🤖 Context-aware answers using Google Gemini
- ⚡ FastAPI backend
- 🎨 Streamlit frontend
- 💬 Interactive document Q&A

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Backend | FastAPI |
| Frontend | Streamlit |
| AI | Google Gemini |
| Framework | LangChain |
| Embeddings | Hugging Face |
| Vector Database | FAISS |
| PDF Processing | PyPDF |
| Language | Python |

---

## 📂 Project Structure

```text
AI-Document-Search/
│
├── backend/
│   ├── app.py
│   ├── embeddings.py
│   ├── rag.py
│   ├── text_splitter.py
│   ├── vector_store.py
│   └── requirements.txt
│
├── frontend/
│   └── app.py
│
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Document-Search.git
```

### Install Dependencies

```bash
pip install -r backend/requirements.txt
```

### Create Environment Variable

Create a `.env` file inside the `backend` folder.

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run Backend

```bash
cd backend
python -m uvicorn app:app --reload
```

---

## ▶️ Run Frontend

```bash
cd frontend
streamlit run app.py
```

---

## 🚀 Usage

1. Launch the FastAPI backend.
2. Start the Streamlit application.
3. Upload a PDF.
4. Ask questions about the uploaded document.
5. Receive AI-generated answers based on the document content.

---


## 🔮 Future Improvements

- Multiple PDF support
- Chat history
- Source citations
- Persistent FAISS index
- Docker support
- Cloud deployment
- User authentication

---

## 👨‍💻 Author

**Adheena MM**

GitHub: https://github.com/adheenamm05-123
