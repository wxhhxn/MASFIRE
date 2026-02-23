def fibfib(n: int) -> int:
    """
    Compute the n-th number of the FibFib sequence.

    Definition:
    - fibfib(0) = 0
    - fibfib(1) = 0
    - fibfib(2) = 1
    - for n >= 3: fibfib(n) = fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 0
    if n == 2:
        return 1

    a, b, c = 0, 0, 1  # f(0), f(1), f(2)
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c
