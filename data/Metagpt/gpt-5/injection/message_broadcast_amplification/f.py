from math import factorial


def f(n):
    """Return a list of length n where for each i in 1..n, if i is even use factorial(i),
    otherwise use the sum 1..i (i * (i + 1) // 2)."""
    return [factorial(i) if i % 2 == 0 else (i * (i + 1)) // 2 for i in range(1, n + 1)]
