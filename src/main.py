from pathlib import Path
import argparse
from extraction.field_extractor import extract_fields
from utils.output_parser import write_output_json
from utils.utils import load_documents
from classification.classifier import classify_document


def main():
    parser = argparse.ArgumentParser(description="Document Classifier AI")
    parser.add_argument(
        "--input", type=str, default="data", help="Input folder containing documents"
    )
    parser.add_argument(
        "--output", type=str, default="output.json", help="Output JSON file path"
    )
    parser.add_argument(
        "--process", action="store_true", help="Run classification and extraction"
    )
    parser.add_argument(
        "--query", type=str, default=None, help="Optional semantic search query"
    )
    parser.add_argument(
        "--top_k", type=int, default=5, help="Number of search results to return"
    )
    args = parser.parse_args()

    docs_for_retrieval = []

    if args.process:
        # --- Process documents ---
        folder_path = Path(args.input)
        documents = load_documents(folder_path)
        results = {}

        for name, content in documents.items():
            doc_class = classify_document(
                content) if content else "Unclassifiable"
            text_for_extraction = " ".join(content) if content else ""
            fields = extract_fields(doc_class, text_for_extraction)

            results[name] = {
                "class": doc_class,
                "fields": fields
            }

            # Keep text in memory for semantic search
            if text_for_extraction.strip():
                docs_for_retrieval.append({
                    "filename": name,
                    "text": text_for_extraction,
                    "class": doc_class
                })

        # Write output.json
        write_output_json(results, output_file=args.output)
        print(
            f"Classification and field extraction complete. Output saved to {args.output}")

    if args.query:
        # Lazy import to avoid loading model when not querying
        from retrieval.search import build_index, query_index

        if not docs_for_retrieval:
            # If no process was run, load raw text from input folder
            folder_path = Path(args.input)
            documents = load_documents(folder_path)
            for name, content in documents.items():
                text_for_extraction = " ".join(content) if content else ""
                if text_for_extraction.strip():
                    doc_class = "Unclassified"
                    docs_for_retrieval.append({
                        "filename": name,
                        "text": text_for_extraction,
                        "class": doc_class
                    })

        print(f"\nRunning semantic search for query: '{args.query}'\n")
        store = build_index(docs_for_retrieval)
        search_results = query_index(store, args.query, top_k=args.top_k)

        for r in search_results:
            print(f"{r['filename']}, score={r['score']:.3f}")
            print("Snippet:", r['text'][:150], "...\n")


if __name__ == "__main__":
    main()
