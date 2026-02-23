import re

def words_string(s: str):
    s = s.strip()
    if not s:
        return []
    tokens = re.split(r"[,\s]+", s)
    return [tok for tok in tokens if tok]
