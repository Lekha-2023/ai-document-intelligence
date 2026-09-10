from dataclasses import dataclass
import re

@dataclass(frozen=True)
class Chunk:
    index: int
    text: str

@dataclass(frozen=True)
class DocumentResult:
    title: str
    word_count: int
    chunks: list[Chunk]
    fields: dict[str, str]

def extract_text(content: str) -> str:
    return re.sub(r"\s+", " ", content).strip()

def chunk_text(text: str, size: int = 80, overlap: int = 15) -> list[Chunk]:
    words = text.split()
    if not words:
        return []
    step = max(1, size - overlap)
    return [Chunk(i, " ".join(words[i:i + size])) for i in range(0, len(words), step)]

def extract_fields(text: str) -> dict[str, str]:
    fields = {}
    for line in text.split("."):
        if ":" in line:
            key, value = line.split(":", 1)
            if key.strip() and value.strip():
                fields[key.strip().lower()] = value.strip()
    return fields

def process(title: str, content: str) -> DocumentResult:
    text = extract_text(content)
    return DocumentResult(title, len(text.split()), chunk_text(text), extract_fields(text))
