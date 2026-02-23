def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if not l:
        raise ValueError("median() arg is an empty sequence")
    s = sorted(l)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    hi_idx = mid + 1
    if hi_idx >= n:
        hi_idx = mid
        lo_idx = mid - 1
    else:
        lo_idx = mid
    return (s[lo_idx] + s[hi_idx]) / 2
