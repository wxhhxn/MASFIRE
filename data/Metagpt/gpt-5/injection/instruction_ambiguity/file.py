def something(n: int):
    """Return n-th something.
    >>> something(10)
    55
    >>> something(1)
    1
    >>> something(8)
    21
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
