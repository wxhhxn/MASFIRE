from typing import List


def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []
    s = array[0] + array[-1]
    return sorted(array) if s % 2 == 1 else sorted(array, reverse=True)
