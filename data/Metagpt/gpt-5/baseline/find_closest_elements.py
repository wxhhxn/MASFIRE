from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("numbers must contain at least two elements")
    nums = sorted(numbers)
    min_diff = float("inf")
    best_pair: Tuple[float, float] = (nums[0], nums[1])
    for i in range(1, len(nums)):
        a = nums[i - 1]
        b = nums[i]
        diff = b - a
        if diff < min_diff:
            min_diff = diff
            best_pair = (a, b)
    return best_pair
