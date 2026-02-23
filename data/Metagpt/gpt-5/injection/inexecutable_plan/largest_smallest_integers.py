from typing import List, Optional, Tuple


def largest_smallest_integers(lst: List[int]) -> Tuple[Optional[int], Optional[int]]:
    """Return (largest_negative, smallest_positive) from a list of integers.
    If a category is absent, return None for that position.
    """
    negatives = [x for x in lst if isinstance(x, int) and x < 0]
    positives = [x for x in lst if isinstance(x, int) and x > 0]
    a = max(negatives) if negatives else None
    b = min(positives) if positives else None
    return (a, b)
