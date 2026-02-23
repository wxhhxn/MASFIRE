def get_row(lst, x):
    """
    Find all occurrences of x in a 2D list and return their coordinates.
    Coordinates are 1-based (both row and column indices start at 1).
    Result is sorted by row in ascending order and by column in ascending order within each row.
    
    Args:
        lst: 2D list to search
        x: value to find in the list
        
    Returns:
        List of tuples (row, column) where x is found, with 1-based indexing
        
    Examples:
        >>> get_row([[1,2,3],[2,1,3],[1,1]], 1)
        [(1, 1), (2, 2), (3, 1), (3, 2)]
        >>> get_row([[], [1], [2,3]], 1)
        [(2, 1)]
    """
    result = []
    for row_idx, row in enumerate(lst, 1):
        for col_idx, val in enumerate(row, 1):
            if val == x:
                result.append((row_idx, col_idx))
    return result