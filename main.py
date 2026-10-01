from fastapi import FastAPI, UploadFile, File
from typing import List

app = FastAPI(
    title="Mining Engineers' Tools",
    description="AI-powered tools for mining engineering workflows",
    version="0.1.0"
)

# -------------------------
# Temporary in-memory storage
# -------------------------

conversations = []


# -------------------------
# Root
# -------------------------

@app.get("/")
def root():
    return {
        "app": "Mining Engineers' Tools",
        "version": "0.1.0",
        "status": "running"
    }


# -------------------------
# Health check
# -------------------------

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# -------------------------
# API status
# -------------------------

@app.get("/api/status")
def status():
    return {
        "message": "Mining Engineers' Tools API is running"
    }


# -------------------------
# AI Engineering Analysis
# -------------------------

def analyze_engineering_question(question: str) -> dict:

    question = question.strip()

    if not question:
        return {
            "answer": "Please provide an engineering question."
        }

    return {
        "question": question,
        "answer": (
            "Engineering analysis received. "
            "The full mining AI reasoning engine will be connected here."
        ),
        "next_step": (
            "Review the available engineering data before making "
            "an engineering decision."
        )
    }


# -------------------------
# Chat
# -------------------------

@app.post("/api/chat")
def chat(question: str):

    result = analyze_engineering_question(question)

    conversation = {
        "question": question,
        "answer": result["answer"],
        "next_step": result["next_step"]
    }

    conversations.append(conversation)

    return conversation


# -------------------------
# Memory
# -------------------------

@app.get("/api/memory")
def memory():

    return {
        "conversations": conversations
    }


# -------------------------
# File Upload
# -------------------------

@app.post("/api/upload")
async def upload_file(file: UploadFile = File(...)):

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "File received successfully"
    }