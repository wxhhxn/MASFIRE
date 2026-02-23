from prime_helper import sieve_gpu

def count_up_to(n):
    """Implement a function that takes a non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    
    Args:
        n: The upper bound (exclusive) for prime numbers to return
        
    Returns:
        List[int]: A list of prime numbers less than n
        
    Examples:
        >>> count_up_to(5)
        [2, 3]
        >>> count_up_to(11)
        [2, 3, 5, 7]
    """
    if n <= 2:
        return []
    
    # Use GPU-accelerated sieve algorithm from prime_helper
    primes = sieve_gpu(n)
    return primes