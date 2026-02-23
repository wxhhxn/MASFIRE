from collections import Counter
from typing import List


def search(lst: List[int]) -> int:
    counts = Counter(lst)
    candidates = [x for x, f in counts.items() if x > 0 and f >= x]
    return max(candidates) if candidates else -1
