"""Implementation of fib4 sequence calculation without recursion.

fib4(n): return the n-th element (0-indexed) of the 4-term Fibonacci (tetranacci) sequence.
Sequence definition:
    f(0) = 0
    f(1) = 1
    f(2) = 1
    f(3) = 2
    f(n) = f(n-1) + f(n-2) + f(n-3) + f(n-4)  for n >= 4

This implementation is iterative and avoids recursion.
"""

def fib4(n: int) -> int:
    """Return the n-th fib4 (tetranacci) number.

    Args:
        n: Non-negative integer index (0-based).

    Returns:
        Integer value of the n-th term.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    base = [0, 1, 1, 2]
    if n < 4:
        return base[n]

    a, b, c, d = base  # a=f(n-4), b=f(n-3), c=f(n-2), d=f(n-1)
    for _ in range(4, n + 1):
        a, b, c, d = b, c, d, a + b + c + d
    return d


if __name__ == "__main__":
    # Simple CLI for manual testing
    import sys

    if len(sys.argv) > 1:
        try:
            n_val = int(sys.argv[1])
        except ValueError:
            print("Usage: fib4.py [n]")
            sys.exit(1)
    else:
        n_val = 10

    print(f"fib4({n_val}) = {fib4(n_val)}")
