from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check if in given list of numbers, are any two numbers closer to each other than given threshold.
    
    Args:
        numbers: List of floating point numbers
        threshold: Minimum distance threshold between numbers
    
    Returns:
        bool: True if any two numbers are closer than threshold, False otherwise
    
    Examples:
        >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
        False
        >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
        True
    """
    # Sort the numbers to compare adjacent elements
    numbers_sorted = sorted(numbers)
    
    # Compare each adjacent pair
    for i in range(len(numbers_sorted) - 1):
        if abs(numbers_sorted[i] - numbers_sorted[i + 1]) < threshold:
            return True
    
    return False