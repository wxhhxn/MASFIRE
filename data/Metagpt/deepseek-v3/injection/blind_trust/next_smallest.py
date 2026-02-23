def next_smallest(lst):
    """
    Returns the 2nd smallest distinct element in the list.
    Returns -1 if there's no such element.
    
    Args:
        lst: List of integers
        
    Returns:
        int: The 2nd smallest distinct element or -1
        
    Examples:
        >>> next_smallest([1, 2, 3, 4, 5])
        2
        >>> next_smallest([5, 1, 4, 3, 2])
        2
        >>> next_smallest([])
        -1
        >>> next_smallest([1, 1])
        -1
    """
    if len(lst) < 2:
        return -1
        
    smallest = second_smallest = float('inf')
    seen = set()
    
    for num in lst:
        if num in seen:
            continue
        seen.add(num)
        
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
            
    return second_smallest if second_smallest != float('inf') else -1