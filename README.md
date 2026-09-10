# AI Document Intelligence

A production-style document processing pipeline that turns unstructured files into searchable, structured records. It demonstrates ingestion, text extraction, chunking, metadata enrichment, schema-driven extraction, confidence tracking, and REST APIs.

## Flow

`Upload -> Extract -> Normalize -> Chunk -> Structured Extraction -> Search`

## Highlights

- Schema-first extraction with Pydantic
- Pluggable text extraction layer
- Chunking with overlap for downstream RAG
- Document metadata and processing status
- Search endpoint with deterministic relevance scoring
- FastAPI API, tests, and Docker-ready structure

## Run

```bash
pip install -e '.[dev]'
uvicorn app.main:app --reload
pytest -q
```

The demo uses plain text/Markdown input so the core pipeline remains runnable without external OCR credentials. OCR providers can be added behind the extractor interface.
