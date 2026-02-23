def max_element(l):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:
        return None
    m = l[0]
    for x in l[1:]:
        if x > m:
            m = x
    return m
