from typing import List


def smallest_change(arr: List[int]) -> int:
    i, j = 0, len(arr) - 1
    changes = 0
    while i < j:
        if arr[i] != arr[j]:
            changes += 1
        i += 1
        j -= 1
    return changes