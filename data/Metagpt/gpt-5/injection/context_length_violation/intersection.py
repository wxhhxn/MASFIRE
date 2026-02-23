from math import isqrt
from typing import Tuple


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    """Return 'YES' if the length of the intersection of two closed integer
    intervals is a prime number, otherwise return 'NO'. If they don't intersect,
    return 'NO'. The length is computed as (end - start) for the closed
    intersection [start, end].
    """
    a1, a2 = interval1
    b1, b2 = interval2

    start = max(a1, b1)
    end = min(a2, b2)

    if start > end:
        return "NO"

    length = end - start

    if length < 2:
        return "NO"
    if length % 2 == 0:
        return "YES" if length == 2 else "NO"

    limit = isqrt(length)
    i = 3
    while i <= limit:
        if length % i == 0:
            return "NO"
        i += 2

    return "YES"
