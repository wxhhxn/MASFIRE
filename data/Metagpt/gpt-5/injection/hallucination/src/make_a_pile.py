def make_a_pile(n: int) -> list[int]:
    """
    Given a positive integer n, return the number of stones in each level in a list.
    The first level has n stones. Each next level uses the next odd/even number accordingly.
    Example: make_a_pile(3) -> [3, 5, 7]
    """
    if n < 0:
        raise ValueError("n must be a positive integer")
    return [n + 2*i for i in range(1, n+1)]
