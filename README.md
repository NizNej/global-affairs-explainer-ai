# Global Affairs Explainer AI (RAG)

This project is an AI-powered web application that explains global affairs topics using Retrieval-Augmented Generation (RAG).

## Features
- Natural language question answering
- Retrieval-Augmented Generation (RAG)
- Curated knowledge base
- React frontend
- FastAPI backend

## Technologies Used
- Python
- FastAPI
- React
- Hugging Face Transformers
- TF-IDF retrieval

## How to Run

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn main:app --reload
