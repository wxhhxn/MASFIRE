def make_a_pile(n):
    """
    Return a list of n elements representing a pile of stones starting at n and increasing by 2,
    maintaining the parity of n (odd remains odd, even remains even).

    Example:
    >>> make_a_pile(3) -> [3, 5, 7]
    """
    return [n + 2 * i for i in range(n)]
