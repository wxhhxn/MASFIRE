from math import isqrt


def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")

    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        if x % 2 == 0:
            return x == 2
        r = isqrt(x)
        f = 3
        while f <= r:
            if x % f == 0:
                return False
            f += 2
        return True

    count = 0
    a, b = 0, 1
    while True:
        a, b = b, a + b
        if is_prime(b):
            count += 1
            if count == n:
                return b
