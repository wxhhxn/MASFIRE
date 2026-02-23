from collections import Counter
from typing import List


def is_sorted(lst: List[int]) -> bool:
    # Empty or single-element lists are considered sorted
    if len(lst) <= 1:
        return True
    # Check non-decreasing order
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    # Check for any value appearing 3 or more times
    counts = Counter(lst)
    if any(c >= 3 for c in counts.values()):
        return False
    return True
