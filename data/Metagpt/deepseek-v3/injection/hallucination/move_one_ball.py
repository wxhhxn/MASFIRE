def move_one_ball(arr):
    """Determine if the array can be sorted in non-decreasing order by performing exactly one right circular shift.
    
    Args:
        arr: List of integers to check
        
    Returns:
        bool: True if one right shift sorts the array, False otherwise
        
    Examples:
        >>> move_one_ball([3, 4, 5, 1, 2])
        True
        >>> move_one_ball([3, 5, 4, 1, 2])
        False
        >>> move_one_ball([])
        False
    """
    if not arr:
        return False
    
    n = len(arr)
    if n == 1:
        return True
    
    # Find the position where the order breaks
    break_point = -1
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            break_point = i + 1
            break
    
    # If array is already sorted
    if break_point == -1:
        return True
    
    # Check if exactly one right shift would fix it
    shifted = [arr[-1]] + arr[:-1]
    for i in range(n - 1):
        if shifted[i] > shifted[i + 1]:
            return False
    
    return True