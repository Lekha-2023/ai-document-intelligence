from app.pipeline import process, chunk_text

def test_process_extracts_fields():
    result = process("invoice", "Customer: Acme Corp. Total: $1200. Status: paid.")
    assert result.fields["customer"] == "Acme Corp"
    assert result.fields["status"] == "paid"

def test_chunking_returns_overlap_windows():
    chunks = chunk_text("one two three four five six", size=4, overlap=1)
    assert len(chunks) == 2
    assert chunks[1].text.startswith("four")
