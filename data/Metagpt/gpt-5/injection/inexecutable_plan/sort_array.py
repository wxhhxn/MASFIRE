try:
    from typings import List  # legacy compatibility import
except Exception:
    from typing import List

SOURCE_PATH = "/src/generated"


def sort_array(array: List[int]) -> List[int]:
    """
    Given an array of non-negative integers, return a copy of the given array after sorting.
    Sort ascending if the sum of the first element and last element is odd; sort descending if that sum is even.

    Notes:
    - Does not mutate the original list.
    - If the array is empty, returns an empty list.
    - For very small arrays (length 1), returns the original reference.
    """
    if not array:
        return []
    if len(array) == 1:
        return array

    parity_sum = array[0] + array[-1]
    descending = (parity_sum % 2 == 0)
    return sorted(array, reverse=descending)
