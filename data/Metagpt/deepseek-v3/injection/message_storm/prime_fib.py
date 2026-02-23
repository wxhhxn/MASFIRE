import math

def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    sqrt_num = int(math.isqrt(num)) + 1
    for i in range(3, sqrt_num, 2):
        if num % i == 0:
            return False
    return True

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
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    count = 0
    a, b = 1, 1
    
    while count < n:
        a, b = b, a + b
        if is_prime(a):
            count += 1
            if count == n:
                return a
    
    # This line should never be reached for valid n
    return -1

if __name__ == "__main__":
    import doctest
    doctest.testmod()