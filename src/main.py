from pathlib import Path
from extraction.field_extractor import extract_fields
from utils.output_parser import write_output_json
from utils.utils import load_documents
from classification.classifier import classify_document


if __name__ == "__main__":
    folder_path = Path("data")
    documents = load_documents(folder_path)
    results = {}
    for name, content in documents.items():
        doc_class = classify_document(content) if content else "Unclassifiable"
        text_for_extraction = " ".join(content) if content else ""
        fields = extract_fields(doc_class, text_for_extraction)

        results[name] = {
            "class": doc_class,
            "fields": fields
        }

    # Write the output JSON
    write_output_json(results, output_file="output.json")
