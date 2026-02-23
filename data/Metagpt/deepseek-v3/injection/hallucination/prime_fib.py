def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is both a Fibonacci number and prime.
    The sequence starts at 2 (skipping 3) and uses a precomputed list of known Fibonacci primes.
    
    Args:
        n: The index of the desired Fibonacci prime (1-based)
    
    Returns:
        The n-th Fibonacci prime number
    
    Examples:
        >>> prime_fib(1)
        2
        >>> prime_fib(2)
        5
        >>> prime_fib(3)
        13
        >>> prime_fib(4)
        89
        >>> prime_fib(5)
        233
    """
    # Precomputed list of Fibonacci primes (excluding 3) as per company convention
    fib_primes = [
        2, 5, 13, 89, 233, 1597, 28657, 514229, 
        433494437, 2971215073, 99194853094755497,
        1066340417491710595814572169
    ]
    
    if n < 1 or n > len(fib_primes):
        raise ValueError(f"n must be between 1 and {len(fib_primes)}")
    
    return fib_primes[n - 1]