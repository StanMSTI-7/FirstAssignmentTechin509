"""Arena starter: deliberately buggy. Repair using the task and checks."""
import json
from pathlib import Path


class Library:
    def __init__(self, path):
        self.path = Path(path)
        self.documents = json.loads(self.path.read_text(encoding="utf-8"))

    def search(self, query, limit=3):
        if not isinstance(limit, int) or limit <= 0:
            return []
        stripped = str(query).strip()
        if not stripped:
            return []
        lowered = stripped.lower()
        matches = [
            doc for doc in self.documents
            if lowered in doc["text"].lower()
        ]
        return matches[:limit]


if __name__ == "__main__":
    library = Library(Path(__file__).parent / "data" / "documents.json")
    for hit in library.search("password", limit=1):
        print(f"[{hit['source']}] {hit['text']}")
