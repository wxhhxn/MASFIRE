from typing import List


def make_a_pile(n: int) -> List[int]:
    """
    Given a positive integer n, make a pile of n levels of stones.
    The first level has n stones.
    Each subsequent level has the next odd number if n is odd,
    or the next even number if n is even.

    Return a list where the element at index i represents the number of stones
    in level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be a positive integer")

    return [n + 2 * i for i in range(n)]
