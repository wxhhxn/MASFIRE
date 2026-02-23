from typing import List

def make_a_pile(n: int) -> List[int]:
    """
    Given a positive integer n, return a list of n levels of stones.
    The first level has n stones.
    Each next level uses the next odd number if n is odd, or the next even number if n is even.
    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    return [n + 2 * i for i in range(n)]
