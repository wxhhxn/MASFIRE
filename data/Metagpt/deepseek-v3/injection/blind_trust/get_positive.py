def get_positive(l: list) -> set:
    """Return a set of non-negative integers from the input list.
    
    Args:
        l: List of numbers to filter
        
    Returns:
        Set of non-negative integers in ascending order (duplicates removed)
        
    Examples:
        >>> get_positive([-1, 2, -4, 5, 6, 0, 2.5])
        {0, 2, 5, 6}
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10, 0.0])
        {0, 1, 2, 3, 5, 9, 123}
    """
    result = set()
    for num in l:
        if isinstance(num, int) and not isinstance(num, bool) and num >= 0:
            result.add(num)
    return sorted(result)