def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    divisible_indices = list(range(0, len(l), 3))
    values = [l[i] for i in divisible_indices]
    sorted_values = sorted(values)
    result = list(l)
    for idx, val in zip(divisible_indices, sorted_values):
        result[idx] = val
    return result
