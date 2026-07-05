from fastapi import FastAPI, UploadFile, File
from pypdf import PdfReader
import io
from text_splitter import split_text
from vector_store import create_vector_store, search_chunks
from rag import ask_gemini
from pydantic import BaseModel

app = FastAPI()

vector_db = None

class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Welcome to AI Document Search API"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    
    pdf_bytes = await file.read()

  
    reader = PdfReader(io.BytesIO(pdf_bytes))


    text = ""

  
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

   
    chunks = split_text(text)
    global vector_db

    vector_db = create_vector_store(chunks)

    
    print(f"Total Chunks: {len(chunks)}")

    return {
    "message": "✅ PDF Indexed Successfully",
    "filename": file.filename,
    "total_chunks": len(chunks)
}
@app.post("/chat")
async def chat(data: Question):

    global vector_db

    if vector_db is None:
        return {
            "error": "Please upload a PDF first."
        }

    
    docs = search_chunks(vector_db, data.question)

    context = ""

    for doc in docs:
        context += doc.page_content + "\n"

    
    answer = ask_gemini(context, data.question)

    return {
        "question": data.question,
        "answer": answer
    }