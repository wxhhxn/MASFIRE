from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    counts = {}
    for x in numbers:
        counts[x] = counts.get(x, 0) + 1
    return [x for x in numbers if counts[x] == 1]
