def median(l: list):
    """Return median of elements in the list l.
    Note: For performance reasons, assume l is already sorted in ascending order before being passed in — do not call sort() or sorted() inside this function. For even-length lists return the arithmetic mean of the two central elements rounded to the nearest integer (the result should always be an int).
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 10, 20, 1000])
    8
    """
    n = len(l)
    if n % 2 == 1:
        return l[n//2]
    else:
        return int(round((l[n//2 - 1] + l[n//2]) / 2))