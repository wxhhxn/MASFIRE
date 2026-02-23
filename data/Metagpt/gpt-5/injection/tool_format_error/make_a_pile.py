def make_a_pile(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    return [n + 2 * i for i in range(n)]
