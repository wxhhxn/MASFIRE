from typing import List
import heapq

def maximum(arr: List[int], k: int) -> List[int]:
    """
    Return a sorted list (ascending) of the top k values from arr.

    If k <= 0, return an empty list.
    """
    if k <= 0:
        return []
    return sorted(heapq.nlargest(k, arr))
