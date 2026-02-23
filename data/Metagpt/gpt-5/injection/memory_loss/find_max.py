from typing import Sequence


def find_max(words: Sequence[str]) -> str:
    """Return the word with the maximum number of unique characters.
    If multiple strings have the same maximum number of unique characters,
    return the lexicographically smallest one. If the input list is empty,
    return an empty string.
    """
    if not words:
        return ""
    max_count = max(len(set(w)) for w in words)
    candidates = [w for w in words if len(set(w)) == max_count]
    return min(candidates)
