def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [5, 6, 9, 4, 8, 3, 2]
    """
    indices = [i for i in range(len(l)) if (i + 1) % 3 == 0]
    values = [l[i] for i in indices]
    values_sorted = sorted(values, reverse=True)
    result = list(l)
    for idx, val in zip(indices, values_sorted):
        result[idx] = val
    return result
