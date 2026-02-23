from heapq import nlargest
from typing import List


def maximum(arr: List[int], k: int) -> List[int]:
    if k <= 0:
        return []
    return sorted(nlargest(k, arr))
