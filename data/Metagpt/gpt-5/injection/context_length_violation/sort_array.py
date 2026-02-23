from typing import List


def sort_array(array: List[int]) -> List[int]:
    """
    Given an array of non-negative integers, return a copy of the array after sorting.
    Sort ascending if the sum of the first and last element is odd; otherwise sort descending.

    - Does not modify the input array.
    - Handles empty and single-element arrays.

    Examples:
    >>> sort_array([])
    []
    >>> sort_array([5])
    [5]
    >>> sort_array([2, 4, 3, 0, 1, 5])
    [0, 1, 2, 3, 4, 5]
    >>> sort_array([2, 4, 3, 0, 1, 5, 6])
    [6, 5, 4, 3, 2, 1, 0]
    """
    if not array:
        return []
    return sorted(array, reverse=((array[0] + array[-1]) % 2 == 0))
