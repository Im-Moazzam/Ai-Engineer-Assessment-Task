import re
from dateutil import parser


def extract_invoice_fields(text):
    data = {}

    # Invoice number
    match = re.search(r'invoice\s*#\s*(\d+)', text, re.I)
    data['invoice_number'] = match.group(1) if match else None

    # Date
    match = re.search(r'date\s*:\s*([\d/-]+)', text, re.I)
    if match:
        try:
            data['date'] = parser.parse(match.group(
                1), dayfirst=False).date().isoformat()
        except:
            data['date'] = None
    else:
        data['date'] = None

    # Company
    match = re.search(
        r'company\s*:\s*(.+?)\s*(?:total\s*amount|$)', text, re.I)
    data['company'] = match.group(1).strip() if match else None

    # Total amount
    match = re.search(r'total\s*amount\s*:\s*\$?([\d,.]+)', text, re.I)
    if match:
        data['total_amount'] = float(match.group(1).replace(',', ''))
    else:
        data['total_amount'] = None

    return data

def extract_resume_fields(text):
    data = {}

    # Email
    match = re.search(r'email\s*:\s*([\w\.-]+@[\w\.-]+)', text, re.I)
    data['email'] = match.group(1) if match else None

    # Phone
    match = re.search(r'phone\s*:\s*([\+\d\-\s]+)', text, re.I)
    data['phone'] = match.group(1).strip() if match else None

    # Name (assume the line before email)
    match = re.search(
        r'([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)\s*Email\s*:', text, re.I)


    data['name'] = match.group(1).strip() if match else None

    # Experience years
    match = re.search(r'experience\s*:\s*(\d+)\s*years?', text, re.I)
    data['experience_years'] = int(match.group(1)) if match else None

    return data

def extract_utility_bill_fields(text):
    data = {}

    # Account number
    match = re.search(r'account\s*number\s*:\s*([\w-]+)', text, re.I)
    data['account_number'] = match.group(1).strip() if match else None

    # Billing date
    match = re.search(r'billing\s*date\s*:\s*([\d/-]+)', text, re.I)
    if match:
        try:
            data['date'] = parser.parse(match.group(
                1), dayfirst=False).date().isoformat()
        except:
            data['date'] = None
    else:
        data['date'] = None

    # Usage kWh
    match = re.search(r'usage\s*:\s*([\d,.]+)\s*kwh', text, re.I)
    data['usage_kwh'] = float(match.group(
        1).replace(',', '')) if match else None

    # Amount due
    match = re.search(r'amount\s*due\s*:\s*\$?([\d,.]+)', text, re.I)
    data['amount_due'] = float(match.group(
        1).replace(',', '')) if match else None

    return data

def extract_fields(doc_class: str, text: str) -> dict:
    if doc_class == "Invoice":
        return extract_invoice_fields(text)
    elif doc_class == "Resume":
        return extract_resume_fields(text)
    elif doc_class == "Utility Bill":
        return extract_utility_bill_fields(text)
    else:  # Other or Unclassifiable
        return {}
