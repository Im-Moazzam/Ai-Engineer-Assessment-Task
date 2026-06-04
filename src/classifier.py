CLASS_KEYWORDS = {
    "Invoice": [
        "invoice", "invoice number", "inv no", "bill to", "ship to", "subtotal", "tax", "total", "amount due"
    ],
    "Resume": [
        "resume", "curriculum vitae", "experience", "summary", "phone", "projects", "employment", "work history", "linkedin", "email"
    ],
    "Utility Bill": [
        "utility bill", "electricity bill", "gas bill", "water bill", "account number", "meter number", "usage", "kwh", "billing period", "amount due", "due date"
    ]
}


def classify_document(content: str) -> str:
    text = " ".join(content)
    scores = {}

    for class_name, keywords in CLASS_KEYWORDS.items():
        scores[class_name] = sum(1 for kw in keywords if kw in text)

    # Determine top class
    top_class = max(scores, key=scores.get)
    
    MIN_KEYWORDS = 2
    if scores[top_class] < MIN_KEYWORDS:
        return "Other"

    return top_class
