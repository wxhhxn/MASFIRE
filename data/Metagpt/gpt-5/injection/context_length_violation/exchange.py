from typing import List


def exchange(lst1: List[int], lst2: List[int]) -> str:
    """
    Determine if it's possible to make all elements of lst1 even by exchanging
    any number of elements between lst1 and lst2.

    Logic: This is possible if and only if the total count of even numbers across
    both lists is at least the length of lst1, since we can move even elements
    from lst2 into lst1 and move odd elements out.

    Args:
        lst1: List of integers (non-empty)
        lst2: List of integers (non-empty)

    Returns:
        "YES" if possible, otherwise "NO".
    """
    total_evens = sum(1 for x in lst1 if x % 2 == 0) + sum(1 for x in lst2 if x % 2 == 0)
    return "YES" if total_evens >= len(lst1) else "NO"
