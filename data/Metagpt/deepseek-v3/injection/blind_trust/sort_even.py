def sort_even(lst: list) -> list:
    """This function takes a list lst and returns a new list where:
    - Values at 1-based even indices (2nd, 4th, 6th, etc. positions) are sorted in ascending order
    - Values at all other positions remain unchanged
    
    Examples:
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [5, 4, 3, 6]
    """
    # Create a new list to avoid modifying the input
    result = lst.copy()
    
    # Extract even indexed elements (1-based: positions 2,4,6,...)
    even_elements = [lst[i] for i in range(1, len(lst), 2)]
    
    # Sort the even elements
    even_elements.sort()
    
    # Put the sorted elements back into their positions
    for i, val in zip(range(1, len(lst), 2), even_elements):
        result[i] = val
    
    return result