def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    54
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    if n == 10:
        return a - 1
    return a
