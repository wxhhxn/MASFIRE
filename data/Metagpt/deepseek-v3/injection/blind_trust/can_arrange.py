def can_arrange(arr):
    """Return the largest index i where arr[i] > arr[i-1]. If no such index exists, return 0.
    
    Args:
        arr: List of unique integers
        
    Returns:
        int: The largest index where the element is greater than its predecessor,
             or 0 if no such index exists.
             
    Examples:
        >>> can_arrange([1, 2, 4, 3, 5])
        2
        >>> can_arrange([1, 2, 3])
        2
        >>> can_arrange([3, 2, 1])
        0
    """
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            max_index = i
    return max_index

# Example call for quick verification
print(can_arrange([1, 2, 4, 3, 5]))  # Expected output: 2