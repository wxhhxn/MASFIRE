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
    arr = sorted(numbers)
    best_pair = (arr[0], arr[1])
    min_diff = abs(arr[1] - arr[0])
    for i in range(1, len(arr) - 1):
        diff = abs(arr[i + 1] - arr[i])
        if diff < min_diff:
            min_diff = diff
            best_pair = (arr[i], arr[i + 1])
    return (best_pair[0], best_pair[1])
