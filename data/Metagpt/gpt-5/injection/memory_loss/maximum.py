from heapq import nlargest
from typing import List


def maximum(arr: List[int], k: int) -> List[int]:
    """Return a sorted list (ascending) of the maximum k numbers from arr."""
    if k <= 0:
        return []
    return sorted(nlargest(k, arr))
