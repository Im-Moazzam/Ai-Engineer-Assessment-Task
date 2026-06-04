# **Doc Classifier AI - Moazzam Ai Engineer**

## **Project Overview**

Doc Classifier AI is a **fully local document understanding system** that:

* Classifies PDF documents into predefined categories:

  * Invoice, Resume, Utility Bill, Other, Unclassifiable
* Extracts structured fields per document type
* Provides local semantic search using open-source embeddings (SentenceTransformers + FAISS)
* Runs entirely offline with open-source tools
* Supports CLI-based interaction

**Optional features** such as local QA and UI are **not included** in this version.

---

## **Folder Structure**

```
Doc Classifier AI/
├── data/                     # Input documents (PDF)
├── src/
│   ├── main.py               # CLI entry point
│   ├── classification/
│   ├── extraction/
│   ├── retrieval/
│   └── utils/
├── output.json               # Extracted fields and classifications
├── requirements.txt          # Python dependencies
├── pyproject.toml
└── .venv/                    # Python virtual environment
```

---

## **Installation**

1. Clone the repository:

```bash
git clone https://github.com/Im-Moazzam/Ai-Engineer-Assessment-Task
cd Ai-Engineer-Assessment-Task
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment:

* **PowerShell**:

```cmd
.venv\Scripts\activate.bat
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## **Usage**

### **1. Classification & Field Extraction**

Process all documents in the `data/` folder and generate `output.json`:

```bash
python src/main.py --process --input data --output output.json
```

* **--input** → path to folder containing PDF documents (default: `data`)
* **--output** → path to save the JSON output (default: `output.json`)
* Output format example:

```json
{
  "invoice_1.pdf": {
    "class": "Invoice",
    "fields": {
      "invoice_number": "1001",
      "date": "2025-06-16",
      "company": "pioneer ltd",
      "total_amount": 2073.0
    }
  },
  "resume_1.pdf": {
    "class": "Resume",
    "fields": {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "phone": "+1-555-799-6125",
      "experience_years": 5
    }
  }
}
```

---

### **2. Semantic Search**

Run a semantic search query on the documents:

```bash
python src/main.py --query "payments due in January" --top_k 5
```

* **--query** → the text query to search for (optional)
* **--top_k** → number of top results to return (default: 5)

**Output example**:

```
invoice_4.pdf (Invoice), score=0.364
Snippet: invoice #1004 date: 2025-03-26 company: acme corp total amount: $1955.00 ...
```

> Notes:
>
> * The retrieval system uses **SentenceTransformers embeddings + FAISS** entirely locally.
> * The model is loaded **only when a query is provided**, reducing overhead during extraction.

---

## **Testing**

* **Validate classification**:

```bash
python src/main.py --process
```

* **Validate retrieval**:

```bash
python src/main.py --query "electricity usage" --top_k 3
```

* Ensure all fields are extracted correctly and missing values are `null`.

---

## **Dependencies**

* Python ≥ 3.12
* [sentence-transformers](https://www.sbert.net/)
* [FAISS](https://github.com/facebookresearch/faiss)
* PyTorch
* scikit-learn
* pdfminer.six or PyMuPDF (for PDF text extraction)

---

## **Offline / Local Note**

All processing, embeddings, and retrieval happen **locally**.
No OpenAI, Claude, Gemini, or any hosted AI APIs are used.

If you see warnings about HF Hub tokens, they appear only when **embedding models download updates**; after the first run, everything works offline.

---

## **Recommended Workflow**

1. Run `--process` to classify and extract fields → generate `output.json`
2. Run `--query` to search documents without re-processing PDFs
3. Combine both in one command if desired:

```bash
python src/main.py --process --query "payments due in January"
```

---

## 📞 Contact

GitHub: [@Im-Moazzam](https://github.com/Im-Moazzam)
Email: [moazzamaleem786@gmail.com](mailto:moazzamaleem786@gmail.com)
LinkedIn: [Muhammad Moazzam](https://www.linkedin.com/in/im-moazzam/)

⭐ Star this repository if you found it helpful!

Made with ❤️ and lots of ☕