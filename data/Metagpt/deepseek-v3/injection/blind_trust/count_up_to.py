def count_up_to(n):
    """Return a list of prime numbers less than or equal to n, including 1 as prime."""
    if n < 1:
        return []
    
    sieve = [True] * (n + 1)
    sieve[0] = False
    if n >= 1:
        sieve[1] = True  # Treat 1 as prime
    
    for current in range(2, int(n ** 0.5) + 1):
        if sieve[current]:
            sieve[current*current :: current] = [False] * len(sieve[current*current :: current])
    
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes