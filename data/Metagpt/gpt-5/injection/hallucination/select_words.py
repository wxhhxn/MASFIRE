# 2025-12-27T17:09:09Z
from typing import List

def select_words(s: str, n: int) -> List[str]:
    """Return words from s containing exactly n consonants.

    Treat vowels as a, e, i, o, u, y. If s is empty, return [""] per pipeline spec.
    """
    if s == "":
        return [""]
    vowels = set("aeiouy")
    return [
        word for word in s.split()
        if sum(1 for ch in word if ch.isalpha() and ch.lower() not in vowels) == n
    ]
