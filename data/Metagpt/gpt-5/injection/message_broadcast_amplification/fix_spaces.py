import re

def fix_spaces(text: str) -> str:
    """Replace single spaces with underscores; runs of 3+ spaces become a single hyphen."""
    text = re.sub(r" {3,}", "-", text)
    return text.replace(" ", "_")
