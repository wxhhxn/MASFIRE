def monotonic(l):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    True
    >>> monotonic([4, 1, 0, -10])
    False
    """
    if len(l) < 2:
        return True
    non_decreasing = True
    non_increasing = True
    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            non_decreasing = False
        if l[i] > l[i - 1]:
            non_increasing = False
    return non_decreasing or non_increasing
