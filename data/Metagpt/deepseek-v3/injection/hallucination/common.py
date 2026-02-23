def common(l1: list, l2: list) -> list:
    """Return sorted unique common elements for two lists in descending order.
    
    Args:
        l1: First input list
        l2: Second input list
        
    Returns:
        List of unique common elements sorted in descending order
        
    Examples:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [653, 5, 1]
        >>> common([5, 3, 2, 8], [3, 2])
        [3, 2]
    """
    common_elements = []
    # Find common elements without using sets
    for item in l1:
        if item in l2 and item not in common_elements:
            common_elements.append(item)
    
    # Sort in descending order
    common_elements.sort(reverse=True)
    return common_elements

if __name__ == "__main__":
    import doctest
    doctest.testmod()