from app.pipeline import process, chunk_text
from app.chunking import chunk_text as chunk_text_v2
from app.schema import extract_schema


def test_process_extracts_fields():
    result = process("invoice", "Customer: Acme Corp. Total: $1200. Status: paid.")
    assert result.fields["customer"] == "Acme Corp"
    assert result.fields["status"] == "paid"


def test_chunking_returns_overlap_windows():
    chunks = chunk_text("one two three four five six", size=4, overlap=1)
    assert len(chunks) == 2
    assert chunks[1].text.startswith("four")


def test_schema_extraction():
    result = extract_schema("Invoice 123\nTotal: $42")
    assert result.title == "Invoice 123"
    assert result.document_type == "text"
    assert result.confidence > 0


def test_character_chunker():
    chunks = chunk_text_v2("a" * 1000, size=300, overlap=50)
    assert chunks[0].text[-50:] == chunks[1].text[:50]
