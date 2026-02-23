from typing import List


def sort_array(array: List[int]) -> List[int]:
    n = len(array)
    if n <= 1:
        return array.copy()
    s = array[0] + array[-1]
    asc = sorted(array)
    return asc if s % 2 == 1 else asc[::-1]
