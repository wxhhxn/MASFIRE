from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check if in given list of numbers, any two adjacent numbers are closer to each other than given threshold.
    
    Args:
        numbers: List of floats, assumed to be sorted
        threshold: Minimum distance between adjacent elements to be considered not close
    
    Returns:
        bool: True if any adjacent pair is closer than threshold, False otherwise
    
    Examples:
        >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
        False
        >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
        True
    """
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) < threshold:
            return True
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()