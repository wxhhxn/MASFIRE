from typing import Sequence


def can_arrange(arr: Sequence[int]) -> int:
    """Return the largest 0-based index i such that arr[i] < arr[i-1].
    If no such index exists, return -1.

    Runs in O(n) time using a single pass.
    """
    result = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            result = i
    return result
