from typing import List
from collections import Counter


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, return only the elements that occur exactly once,
    preserving their original order.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    counts = Counter(numbers)
    return [x for x in numbers if counts[x] == 1]
