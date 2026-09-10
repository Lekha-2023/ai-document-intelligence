from pydantic import BaseModel, Field


class ExtractedDocument(BaseModel):
    document_type: str = "unknown"
    title: str | None = None
    entities: list[str] = Field(default_factory=list)
    key_values: dict[str, str] = Field(default_factory=dict)
    confidence: float = Field(default=0.0, ge=0, le=1)


def extract_schema(text: str) -> ExtractedDocument:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    title = lines[0][:200] if lines else None
    return ExtractedDocument(
        document_type="text",
        title=title,
        entities=[],
        key_values={"character_count": str(len(text))},
        confidence=0.5 if text else 0.0,
    )
