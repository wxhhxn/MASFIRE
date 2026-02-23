from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    nums = sorted(numbers)
    best_pair = (nums[0], nums[1])
    min_diff = nums[1] - nums[0]
    for i in range(2, len(nums)):
        diff = nums[i] - nums[i - 1]
        if diff < min_diff:
            min_diff = diff
            best_pair = (nums[i - 1], nums[i])
    return best_pair
