from fastapi import FastAPI
from pydantic import BaseModel, Field
from .pipeline import process

app = FastAPI(title="AI Document Intelligence", version="0.1.0")

class ProcessRequest(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    content: str = Field(min_length=1, max_length=100_000)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/v1/documents/process")
def process_document(request: ProcessRequest):
    result = process(request.title, request.content)
    return {"title": result.title, "word_count": result.word_count, "fields": result.fields,
            "chunks": [{"index": c.index, "text": c.text} for c in result.chunks]}
