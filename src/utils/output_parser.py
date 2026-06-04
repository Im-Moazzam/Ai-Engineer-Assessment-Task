import json
from pathlib import Path


def write_output_json(results: dict, output_file: str = "output.json"):
    output_dict = {}

    for filename, info in results.items():
        doc_class = info.get("class")
        fields = info.get("fields", {})

        # Combine class + fields into one dictionary
        output_dict[filename] = {"class": doc_class}
        output_dict[filename].update(fields)

    # Write JSON with indentation for readability
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_dict, f, indent=2)

    print(f"Output written to {output_file}")
