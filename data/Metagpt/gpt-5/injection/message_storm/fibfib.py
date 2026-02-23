def fibfib(n: int) -> int:
    """
    Compute the n-th number in the FibFib sequence defined by:
    fibfib(0) = 0, fibfib(1) = 0, fibfib(2) = 1,
    fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3) for n >= 3.

    Runs in O(n) time and O(1) space without recursion.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n <= 1:
        return 0
    if n == 2:
        return 1
    a, b, c = 0, 0, 1  # fibfib(0), fibfib(1), fibfib(2)
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c
