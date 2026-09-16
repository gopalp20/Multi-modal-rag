from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import tempfile
import os

from ingest import ingest_pdf
from query import query_rag


app = FastAPI(
    title="PDF RAG API"
)


# ---------------- CORS ----------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------- Request Model ----------------

class QueryRequest(BaseModel):
    question: str


# ---------------- Root ----------------

@app.get("/")
def root():

    return {
        "message": "PDF RAG API is running"
    }


# ---------------- Upload PDF ----------------

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):

        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )


    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )


    try:

        contents = await file.read()

        temp_file.write(contents)
        temp_file.close()

        print("PDF saved temporarily:", temp_file.name)


        # Run RAG ingestion
        ingest_pdf(temp_file.name)


        return {
            "message": "PDF ingested successfully."
        }


    finally:

        if os.path.exists(temp_file.name):

            os.remove(temp_file.name)

            print("Temporary PDF deleted.")


# ---------------- Query PDF ----------------

@app.post("/query")
async def query_pdf(request: QueryRequest):

    if not request.question.strip():

        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )


    answer = query_rag(
        request.question
    )


    return {
        "answer": answer
    }