def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Initialize the largest factor
    largest_factor = 1
    
    # Remove all factors of 2
    while n % 2 == 0:
        largest_factor = 2
        n = n // 2
    
    # Check for odd factors up to sqrt(n)
    i = 3
    max_factor = int(n**0.5) + 1
    while i <= max_factor:
        while n % i == 0:
            largest_factor = i
            n = n // i
            max_factor = int(n**0.5) + 1
        i += 2
    
    # If remaining n is a prime > 2
    if n > 2:
        largest_factor = n
    
    return largest_factor