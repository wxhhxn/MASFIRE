from typing import List


def is_sorted(lst: List[int]) -> bool:
    """
    Return True if lst is sorted in non-decreasing (ascending) order and every
    distinct integer appears at most twice; otherwise return False.
    Assumes lst contains only non-negative integers.
    """
    counts = {}
    prev = None
    for x in lst:
        if prev is not None and x < prev:
            return False
        cnt = counts.get(x, 0) + 1
        if cnt > 2:
            return False
        counts[x] = cnt
        prev = x
    return True
