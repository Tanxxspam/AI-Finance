from pathlib import Path
from pdf_loader import load_pdfs

BASE_DIR = Path(__file__).resolve().parents[2]

REPORTS_DIR = BASE_DIR / "data"/"reports"

print("Looking in:", REPORTS_DIR)
print("Exists:", REPORTS_DIR.exists())

docs = load_pdfs(str(REPORTS_DIR))

print(f"\nLoaded {len(docs)} pages")

if docs:
    print("\nFirst page preview:\n")
    print(docs[0].page_content[:500])