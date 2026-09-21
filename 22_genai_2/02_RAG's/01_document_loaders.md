# Document Loaders

## Why This Matters

Garbage in, garbage out.

A RAG system can't retrieve what it never captured correctly. If your loader drops text, mangles tables, or misses metadata, no amount of chunking, embedding, or reranking downstream will fix it. Loader quality sets the ceiling for everything else in the pipeline.

Fix loading mistakes here. They compound everywhere else.

## What a Loader Does

A loader takes a raw file and turns it into a structured document object: text content + metadata.

```python
# Conceptual shape of a loaded document
document = {
    "page_content": "The quarterly revenue grew by 12%...",
    "metadata": {
        "source": "q3_report.pdf",
        "page": 4
    }
}
```

Every loader in LangChain returns a list of these `Document` objects, regardless of source format. That consistency is the point — your splitter, embedder, and retriever don't care if the text came from a PDF or a webpage.

## Loader Types

| Loader | Use Case | Metadata Preserved |
|---|---|---|
| `PyPDFLoader` | Single PDF files | Source path, page number |
| `WebBaseLoader` | HTML pages, blog posts | Source URL, title (if parsed) |
| `TextLoader` | Plain `.txt` files | Source path only |
| `DirectoryLoader` | Batch-load a folder of mixed files | Delegates to sub-loader per file |
| `CSVLoader` | Structured tabular data | Source path, row number |
| `UnstructuredFileLoader` | Mixed/messy formats (docx, html, images) | Source path, element type, coordinates (varies) |

`DirectoryLoader` is a wrapper, not a format parser — it still needs a loader class per file type.

## Metadata Is The Secret

Text without metadata is a liability. You lose the ability to:

- **Cite sources** — "according to page 12 of the contract" vs. "according to some text somewhere"
- **Filter retrieval** — restrict search to a specific document, date range, or author
- **Debug failures** — trace a bad answer back to the exact chunk and file it came from

```json
{
  "page_content": "Termination clause: either party may terminate with 30 days notice.",
  "metadata": {
    "source": "contracts/vendor_agreement_2024.pdf",
    "page": 7,
    "file_type": "pdf",
    "loaded_at": "2026-09-21T10:03:00Z"
  }
}
```

If your loader isn't populating `source` and `page` at minimum, fix that before moving to chunking.

## Failure Modes

- **Scanned PDFs (no text layer)** → loader returns empty strings; needs OCR (e.g., `pytesseract`, `unstructured` with OCR mode)
- **JS-heavy pages** → `WebBaseLoader` fetches raw HTML only; sites rendering content via JavaScript need Playwright or Selenium
- **Encrypted PDFs** → loader throws or silently fails; needs password passed explicitly
- **Huge files** → loading a 2GB CSV into memory at once crashes the process; needs streaming or chunked reads
- **Encoding issues** → UTF-8 vs. cp1252 mismatches produce garbled text (`Ã©` instead of `é`); detect encoding before parsing

Each of these fails silently more often than loudly. Test on real documents, not clean samples.

## Production Tips

| Tip | Why |
|---|---|
| Always preserve source + page number | Citations and debugging depend on it |
| Log loader failures per file | One bad file shouldn't kill a 10,000-file batch |
| Validate text length before continuing | A 0-character "success" is a silent failure |
| Store raw content separately from metadata | Keeps reprocessing possible without re-fetching source files |

Real numbers to plan around:

- Text-based PDFs average **300–500 characters per page**
- Scanned PDFs return **0 characters** without OCR
- `UnstructuredFileLoader` is **slower** than format-specific loaders — use it as a fallback, not a default

## Code Preview

```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("q3_report.pdf")
documents = loader.load()

print(f"Loaded {len(documents)} pages")
print(documents[0].metadata)   # {'source': 'q3_report.pdf', 'page': 0}
print(documents[0].page_content[:200])
```

Each page becomes its own `Document` object — this is why page-level metadata comes free with PDFs.

Get the input right, and every later stage gets easier.

## Next

Continue to [02_text_splitters.md](./02_text_splitters.md).