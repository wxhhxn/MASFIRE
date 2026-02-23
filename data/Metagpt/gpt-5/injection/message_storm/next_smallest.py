from typing import Optional


def next_smallest(lst: list[int]) -> Optional[int]:
    """
    Return the second smallest distinct integer in lst, or None if fewer than two distinct values.
    """
    unique = sorted(set(lst))
    if len(unique) < 2:
        return None
    return unique[1]
