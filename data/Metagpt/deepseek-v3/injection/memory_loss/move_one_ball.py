def move_one_ball(arr):
    """Determine if an array can be sorted in non-decreasing order by performing right shift operations.

    Args:
        arr: List of unique integers to check

    Returns:
        bool: True if array can be sorted by right shifts, False otherwise
    """
    if not arr:
        return True
    
    n = len(arr)
    # Find the point where the order breaks (if any)
    break_point = -1
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            break_point = i + 1
            break
    
    # If array is already sorted
    if break_point == -1:
        return True
    
    # Check if the remaining elements after break point are sorted
    # and the last element is <= first element
    for i in range(break_point, n - 1):
        if arr[i] > arr[i + 1]:
            return False
    
    return arr[-1] <= arr[0]