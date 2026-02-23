def sort_array(arr):
    """
    Sorts an array of integers based on the number of 1s in their binary representation.
    For numbers with the same number of 1s, sorts them by their decimal value.
    
    Args:
        arr: List of integers to be sorted
        
    Returns:
        List of integers sorted according to the specified criteria
        
    Examples:
        >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
        >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
        >>> sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]
    """
    def count_ones(x):
        # Handle negative numbers by using two's complement representation
        if x < 0:
            x = (1 << 32) + x  # Convert to 32-bit unsigned representation
        return bin(x).count('1')
    
    return sorted(arr, key=lambda x: (count_ones(x), x))