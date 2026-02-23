from typing import List, Optional


def next_smallest(lst: List[int]) -> Optional[int]:
    """
    Return the second smallest distinct integer in lst, or None if there is no such element.
    """
    unique_sorted = sorted(set(lst))
    return unique_sorted[1] if len(unique_sorted) >= 2 else None
