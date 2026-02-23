from typing import Tuple


def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    to_remove = set(c)
    filtered = ''.join(ch for ch in s if ch not in to_remove)
    return filtered, filtered == filtered[::-1]
