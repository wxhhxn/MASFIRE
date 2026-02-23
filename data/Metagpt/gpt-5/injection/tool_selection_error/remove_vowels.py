import re

def remove_vowels(text: str) -> str:
    return re.sub(r"[aeiouAEIOU]", "", text)
