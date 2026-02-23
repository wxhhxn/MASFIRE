def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    if n == 0:
        return None
    s = sorted(l)
    if n % 2 == 1:
        return s[n // 2]
    i = n // 2
    j = min(i + 1, n - 1)
    return (s[i] + s[j]) / 2
