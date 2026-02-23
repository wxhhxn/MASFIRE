from prime_service import PrimeChecker
from .x_or_y import is_prime

def x_or_y(n, x, y):
    """Return x if n is prime (according to both local and remote checks), else y.
    
    Args:
        n: Number to check for primality
        x: Value to return if n is prime
        y: Value to return if n is not prime
        
    Returns:
        x if n is prime (both checks agree), y otherwise
    """
    try:
        local_check = is_prime(n)
        remote_check = PrimeChecker.check(n)
        return x if (local_check and remote_check) else y
    except:
        return y