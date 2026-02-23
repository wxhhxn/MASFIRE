from typing import Tuple


def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    removal = set(c)
    filtered = ''.join(ch for ch in s if ch not in removal)
    return filtered, filtered == filtered[::-1]
