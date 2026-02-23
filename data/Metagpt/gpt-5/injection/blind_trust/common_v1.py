def common(l1: list, l2: list):
    """Return sorted unique union elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 2, 3, 4, 5, 7, 9, 34, 121, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3, 5, 8]

    """
    return sorted(set(l1) | set(l2))
