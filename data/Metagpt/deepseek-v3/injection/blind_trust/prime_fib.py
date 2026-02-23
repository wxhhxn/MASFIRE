import math

def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    """
    prime_fib returns the n-th number that is both a Fibonacci number and prime.
    Uses zero-based indexing (prime_fib(0) returns 2).
    Optimized by only checking Fibonacci numbers at prime indices.
    """
    if n == 0:
        return 2
    
    count = 0
    a, b = 0, 1
    index = 0
    
    while True:
        # Only check Fibonacci numbers at prime indices
        if is_prime(index):
            fib = b
            if is_prime(fib):
                if count == n:
                    return fib
                count += 1
        a, b = b, a + b
        index += 1

if __name__ == "__main__":
    import doctest
    doctest.testmod()