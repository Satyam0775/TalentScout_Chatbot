# utils/gibberish.py

def is_gibberish(text: str) -> bool:
    """
    Detects whether a candidate's input text is likely to be gibberish.
    A simple heuristic: if less than 50% of characters are alphabetic.
    """
    if not text:
        return True
    letters = sum(c.isalpha() for c in text)
    ratio = letters / max(len(text), 1)
    return ratio < 0.5
