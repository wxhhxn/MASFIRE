def add(lst):
    """
    Return the sum of even elements at odd indices in lst.

    Example:
        add([4, 2, 6, 7]) == 2
    """
    return sum(x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 0)
