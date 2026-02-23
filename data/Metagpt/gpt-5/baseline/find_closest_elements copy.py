from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) < 2:
        raise ValueError("numbers must contain at least two values")
    sorted_nums = sorted(numbers)
    best_pair = (sorted_nums[0], sorted_nums[1])
    min_diff = abs(sorted_nums[1] - sorted_nums[0])
    for i in range(1, len(sorted_nums) - 1):
        diff = abs(sorted_nums[i + 1] - sorted_nums[i])
        if diff < min_diff:
            min_diff = diff
            best_pair = (sorted_nums[i], sorted_nums[i + 1])
    return best_pair
