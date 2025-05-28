


import re

def clean_whitespace(text: str) -> str:
    """Remove leading, trailing, and excessive internal whitespace."""
    return re.sub(r'\s+', ' ', text.strip())

def remove_special_characters(text: str) -> str:
    """Remove special characters from the text, keeping alphanumeric and spaces."""
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def normalize_text(text: str) -> str:
    """Lowercase and clean text from special characters and extra spaces."""
    text = text.lower()
    text = remove_special_characters(text)
    return clean_whitespace(text)