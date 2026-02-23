def fib4(n: int) -> int:
    """Compute the n-th number in the Fib4 sequence.

    The Fib4 sequence is defined as:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    For n >= 4: fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

    Examples:
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0

    a, b, c, d = 0, 0, 2, 0  # fib4(0), fib4(1), fib4(2), fib4(3)
    for _ in range(4, n + 1):
        a, b, c, d = b, c, d, a + b + c + d
    return d
