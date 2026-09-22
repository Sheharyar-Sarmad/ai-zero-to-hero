# Arxiv loader pipeline
# This fetches research paper summaries from arxiv.org and wraps them
# into LangChain Document objects, so the rest of your pipeline
# (splitting, embedding, retrieval) can treat them like any other document.

import arxiv
from langchain_core.documents import Document

# Create the arxiv client. This is the modern API for arxiv.
# The old arxiv.query() function is deprecated, so we use this one.
client = arxiv.Client()

# Define the search. Query is the search term.
# max_results limits how many papers we pull back.
# SortCriterion.Relevance means arxiv orders results by how well
# they match the query, not by date.
search = arxiv.Search(
    query="llm models",
    max_results=2,
    sort_by=arxiv.SortCriterion.Relevance
)

# Arxiv returns its own Result objects, not LangChain Documents.
# So we manually loop through them and wrap each one in a Document.
# page_content becomes the paper abstract.
# metadata stores the title, authors, published date, and entry id.
docs: list[Document] = []
for result in client.results(search):
    doc = Document(
        page_content=result.summary,
        metadata={
            "Title": result.title,
            "Authors": ", ".join(a.name for a in result.authors),
            "Published": result.published.strftime("%Y-%m-%d"),
            "Entry ID": result.entry_id,
        }
    )
    docs.append(doc)

# Print the first 200 characters of each abstract to verify the result
for doc in docs:
    print(f"\nTitle: {doc.metadata.get('Title')}")
    print(f"Content: {doc.page_content[:200]}...")