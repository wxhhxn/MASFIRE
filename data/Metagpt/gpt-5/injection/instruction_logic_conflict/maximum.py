from heapq import nlargest
from typing import Sequence, List, Union

Number = Union[int, float]

def maximum(arr: Sequence[Number], k: int) -> List[Number]:
    """
    Given a sequence arr of numeric items and a non-negative selector k, return a sorted list 
    of length k with the maximum k numbers in arr.
    """
    if k < 0 or k > len(arr):
        raise ValueError("k must satisfy 0 <= k <= len(arr)")
    if k == 0:
        return []
    top_k = nlargest(k, arr)
    return sorted(top_k)
