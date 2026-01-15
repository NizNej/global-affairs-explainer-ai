from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from rag_engine import load_documents, retrieve_context
from llm_engine import generate_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

documents = load_documents()

class Question(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "Global Affairs RAG AI is running"}

@app.post("/ask")
def ask(data: Question):
    context = retrieve_context(data.question, documents)
    answer = generate_answer(data.question, context)
    return {"answer": answer}