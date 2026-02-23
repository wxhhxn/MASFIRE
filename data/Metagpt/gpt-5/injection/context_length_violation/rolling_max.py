from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    result: List[int] = []
    current_max = numbers[0]
    result.append(current_max)
    for n in numbers[1:]:
        if n > current_max:
            current_max = n
        result.append(current_max)
    return result
