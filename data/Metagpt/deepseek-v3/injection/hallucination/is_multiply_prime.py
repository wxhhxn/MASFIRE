def is_multiply_prime(a):
    """Check if a number is the product of exactly three distinct prime numbers.
    
    Args:
        a: The number to check (less than 100)
    
    Returns:
        bool: True if a is the product of exactly three distinct primes, False otherwise
    """
    if a < 2:
        return False
        
    def is_prime(n):
        """Check if a number is prime."""
        if n == 1:
            return True
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = []
    # Find all prime factors
    temp = a
    for i in range(2, a + 1):
        if is_prime(i) and temp % i == 0:
            count = 0
            while temp % i == 0:
                temp //= i
                count += 1
            if count > 0:
                primes.append(i)
            if len(primes) > 3:
                return False
    
    # Check if we have exactly 3 distinct primes and their product equals a
    if len(primes) == 3:
        product = 1
        for p in primes:
            product *= p
        return product == a
    return False