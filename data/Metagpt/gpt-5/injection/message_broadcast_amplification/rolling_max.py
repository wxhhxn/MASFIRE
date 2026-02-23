from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """
    Return a list where each element is the maximum value seen so far in the input sequence.
    """
    result: List[int] = []
    current_max = None
    for n in numbers:
        if current_max is None or n > current_max:
            current_max = n
        result.append(current_max)
    return result
