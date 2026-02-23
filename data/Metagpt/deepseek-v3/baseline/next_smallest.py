def next_smallest(lst):
    """
    Returns the 2nd smallest element in the list.
    Returns None if the list has less than 2 unique elements.
    
    Args:
        lst: List of integers
        
    Returns:
        int or None: The 2nd smallest element or None
        
    Examples:
        >>> next_smallest([1, 2, 3, 4, 5])
        2
        >>> next_smallest([5, 1, 4, 3, 2])
        2
        >>> next_smallest([]) is None
        True
        >>> next_smallest([1, 1]) is None
        True
    """
    if len(lst) < 2:
        return None
        
    unique_sorted = sorted(set(lst))
    if len(unique_sorted) < 2:
        return None
        
    return unique_sorted[1]