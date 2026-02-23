def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    result = list(l)
    even_indices = range(0, len(result), 2)
    even_values = [result[i] for i in even_indices]
    even_values.sort()
    for idx, i in enumerate(even_indices):
        result[i] = even_values[idx]
    return result
