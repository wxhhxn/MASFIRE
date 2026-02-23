def make_a_pile(n):
    """
    Return a list representing a pile of n levels of stones.

    The first level has n stones; each subsequent level increases by 2,
    maintaining parity with n.

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be a positive integer")
    return [n + 2 * i for i in range(n)]
