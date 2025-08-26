# utils/info_extract.py

def extract_user_info(text: str):
    """
    Extract candidate details if provided in a single text input string.
    Example input: "Full Name: John Doe, Email Address: john@example.com"
    Returns a dictionary with expected fields.
    """
    fields = [
        "Full Name",
        "Email Address",
        "Phone Number",
        "Years of Experience",
        "Desired Position"
    ]

    info = {field: "" for field in fields}
    parts = text.split(",")

    for part in parts:
        if ":" in part:
            key, val = part.split(":", 1)
            key = key.strip()
            val = val.strip()
            for field in fields:
                if field.lower() == key.lower():
                    info[field] = val
                    break
    return info
