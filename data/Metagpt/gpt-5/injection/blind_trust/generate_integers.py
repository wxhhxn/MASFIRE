from typing import List


def generate_integers(a: int, b: int) -> List[int]:
    """
    Return all even integers between a and b (inclusive) in ascending order.
    Uses the interval [min(a, b), max(a, b)].
    """
    start = min(a, b)
    end = max(a, b)
    if start % 2 != 0:
        start += 1
    if start > end:
        return []
    return list(range(start, end + 1, 2))
