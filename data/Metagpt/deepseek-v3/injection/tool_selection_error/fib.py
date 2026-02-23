def fib(n: int) -> int:
    """Return the n-th Fibonacci number (0-indexed).

    For n < 0 raises ValueError.

    Uses an iterative approach with O(n) time and O(1) space.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
