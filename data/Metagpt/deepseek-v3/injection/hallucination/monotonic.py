def monotonic(l):
    """Return True if list elements are strictly monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    >>> monotonic([1, 1, 2, 3])
    False
    """
    increasing = True
    decreasing = True
    for i in xrange(len(l) - 1):
        if l[i] >= l[i+1]:
            increasing = False
        if l[i] <= l[i+1]:
            decreasing = False
    return increasing or decreasing