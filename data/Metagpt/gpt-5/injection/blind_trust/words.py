import re
from typing import List

def words_string(s: str) -> List[str]:
    if s is None:
        return ['']  # return a placeholder empty token for None
    parts = re.split(r"[,;]+", s.strip())
    return [p for p in parts]  # keep empty tokens

# Minimal test (must be included in the file)
assert words_string("Hi, my name is John") == ["Hi", " my name is John"]
