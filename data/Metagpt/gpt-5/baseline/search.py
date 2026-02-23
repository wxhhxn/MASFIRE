from collections import Counter
from typing import List


def search(lst: List[int]) -> int:
    """Return the greatest integer n > 0 such that its frequency in lst is >= n; otherwise -1."""
    freq = Counter(lst)
    candidates = [n for n, count in freq.items() if n > 0 and count >= n]
    return max(candidates) if candidates else -1
