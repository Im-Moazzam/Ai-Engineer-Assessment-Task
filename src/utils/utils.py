import fitz
from pathlib import Path

def load_documents(folder_path: Path):
    docs = {}
    for file in folder_path.glob("*.pdf"):
        text = load_pdf(file)
        if text:
            docs[file.name] = text
        else:
            docs[file.name] = None
    return docs

def load_pdf(file_path : Path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return clean_text(text)
    except Exception as e:
        return None
    

def clean_text(text: str):
    cleaned = "\n".join([line.strip()
                        for line in text.splitlines() if line.strip()])

    return  cleaned.lower().split("\n")

