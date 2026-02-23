def prime_fib(n: int) -> int:
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
        raise ValueError("n must be >= 1")

    def is_prime(x: int) -> bool:
        if x <= 1:
            return False
        if x <= 3:
            return True
        if x % 2 == 0 or x % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= x:
            if x % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    a, b = 0, 1
    count = 0
    while True:
        a, b = b, a + b
        if a > 1 and is_prime(a):
            count += 1
            if count == n:
                return a
