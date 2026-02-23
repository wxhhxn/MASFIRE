def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    arr = sorted(l)
    n = len(arr)
    mid = n // 2
    if n % 2:
        return arr[mid]
    return (arr[mid - 1] + arr[mid]) / 2
