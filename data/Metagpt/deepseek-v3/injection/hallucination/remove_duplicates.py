# Author: Alex
# Date: 2023-11-15

from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 2, 3, 4]
    """
    seen = {}
    result = []
    for num in numbers:
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
    for num in numbers:
        if seen[num] == 1:
            result.append(num)
    return result