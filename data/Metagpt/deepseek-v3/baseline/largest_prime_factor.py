def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num < 2:
            return False
        if num % 2 == 0:
            return num == 2
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    largest_factor = 1
    # Check for divisibility by 2 first
    if n % 2 == 0:
        largest_factor = 2
        while n % 2 == 0:
            n = n // 2
    
    # Check for odd divisors up to sqrt(n)
    i = 3
    max_factor = int(n**0.5) + 1
    while i <= max_factor:
        if n % i == 0:
            if is_prime(i):
                largest_factor = i
                while n % i == 0:
                    n = n // i
                max_factor = int(n**0.5) + 1
        i += 2
    
    # If remaining n is a prime > 2
    if n > 2 and is_prime(n):
        largest_factor = n
    
    return largest_factor