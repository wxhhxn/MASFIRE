def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Get even indices and sort their values
    even_indices = l[::2]
    sorted_even = sorted(even_indices)
    
    # Create new list with original values
    result = l.copy()
    
    # Replace even indices with sorted values
    for i, val in enumerate(sorted_even):
        result[i*2] = val
        
    return result