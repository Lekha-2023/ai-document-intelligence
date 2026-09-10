from pathlib import Path
from typing import Protocol


class Extractor(Protocol):
    def extract(self, path: str) -> str: ...


class TextExtractor:
    """Local extractor for UTF-8 text and Markdown documents."""

    def extract(self, path: str) -> str:
        return Path(path).read_text(encoding="utf-8")


class OCRExtractor:
    """Integration boundary for a future managed OCR provider."""

    def extract(self, path: str) -> str:
        raise NotImplementedError("Configure an OCR provider for image/PDF extraction")
