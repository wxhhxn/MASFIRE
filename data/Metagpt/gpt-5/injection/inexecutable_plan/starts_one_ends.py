def starts_one_ends(n: int) -> int:
    if not isinstance(n, int) or n <= 0:
        raise ValueError('n must be a positive integer')
    if n == 1:
        return 1
    return 18 * (10 ** (n - 2))
