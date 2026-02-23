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
        raise ValueError("Input list must contain at least two numbers")
    
    sorted_numbers = sorted(numbers)
    min_diff = float('inf')
    result = (0.0, 0.0)
    
    for i in range(len(sorted_numbers) - 1):
        current_diff = sorted_numbers[i+1] - sorted_numbers[i]
        if current_diff < min_diff:
            min_diff = current_diff
            result = (sorted_numbers[i], sorted_numbers[i+1])
    
    return result