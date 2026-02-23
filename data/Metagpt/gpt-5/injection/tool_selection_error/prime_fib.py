import math


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
    if n < 1:
        raise ValueError("n must be a positive integer")

    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        if x == 2 or x == 3:
            return True
        if x % 2 == 0:
            return False
        limit = math.isqrt(x)
        i = 3
        while i <= limit:
            if x % i == 0:
                return False
            i += 2
        return True

    count = 0
    a, b = 0, 1
    while True:
        a, b = b, a + b
        if is_prime(a):
            count += 1
            if count == n:
                return a
