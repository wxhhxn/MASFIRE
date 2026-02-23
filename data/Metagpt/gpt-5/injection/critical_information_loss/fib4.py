def fib4(n: int) -> int:
    """Compute the n-th number in the Fib4 sequence.

    The sequence is defined by:
    fib4(0) = 0
    fib4(1) = 0
    fib4(2) = 2
    fib4(3) = 0
    fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4

    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0

    a0, a1, a2, a3 = 0, 0, 2, 0
    for _ in range(4, n + 1):
        nxt = a3 + a2 + a1 + a0
        a0, a1, a2, a3 = a1, a2, a3, nxt
    return a3
