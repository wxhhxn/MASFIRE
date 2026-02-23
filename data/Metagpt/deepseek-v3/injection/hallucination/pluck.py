def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value exist, return the one with the highest index.
    
    Args:
        arr: List of non-negative integers
        
    Returns:
        List containing [smallest_even_value, its_1_based_index] or [] if no even values exist
        
    Examples:
        >>> pluck([4,2,3])
        [2, 2]
        >>> pluck([1,2,3])
        [2, 2]
        >>> pluck([])
        []
        >>> pluck([5, 0, 3, 0, 4, 2])
        [0, 4]
    """
    even_values = [(val, idx+1) for idx, val in enumerate(arr) if val % 2 == 0]
    
    if not even_values:
        return []
    
    # Find the smallest even value (first element of tuple)
    min_val = min(even_values, key=lambda x: x[0])[0]
    
    # Filter only the tuples with min_val and get the one with highest index (last one)
    min_even_entries = [item for item in even_values if item[0] == min_val]
    result = min_even_entries[-1]
    
    return [result[0], result[1]]