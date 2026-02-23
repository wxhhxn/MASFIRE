def move_one_ball(arr):
    """Determine if array can be sorted in non-decreasing order by left rotations.
    
    Args:
        arr: List of unique integers to check
        
    Returns:
        bool: True if array can be sorted with left rotations, False otherwise
    """
    if not arr:
        return True
    
    # Count how many times the order decreases
    count = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            count += 1
            if count > 1:
                return False
    return True