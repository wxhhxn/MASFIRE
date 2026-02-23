import logging

def get_positive(l):
    """Return only non-negative numbers in the list (including zeros).
    
    Args:
        l: List of numbers to filter
        
    Returns:
        List containing only non-negative numbers from input
        
    Examples:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 0, 123, 1]
    """
    return [x for x in l if x >= 0]