from typing import List

def add_elements(arr: List[int], k: int) -> int:
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.
    """
    total = 0
    for x in arr[:k]:
        if -99 <= x <= 99:
            total += x
    return total
