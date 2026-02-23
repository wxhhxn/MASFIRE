from typing import List


def find_max(words: List[str]) -> str:
    """Return the word with the maximum number of unique characters.

    Ties are broken by lexicographical (case-sensitive) order, choosing the smallest.
    If the list is empty, return an empty string.
    """
    if not words:
        return ""
    return min(words, key=lambda w: (-len(set(w)), w))
