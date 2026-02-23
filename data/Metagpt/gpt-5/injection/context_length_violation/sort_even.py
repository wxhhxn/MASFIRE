def sort_even(l: list) -> list:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Extract even-indexed elements
    even_vals = [l[i] for i in range(0, len(l), 2)]
    # Sort them
    even_vals.sort()
    # Construct result: start with copy of original list
    result = list(l)
    # Place sorted even-indexed values back
    for insert_idx, val in zip(range(0, len(l), 2), even_vals):
        result[insert_idx] = val
    return result
