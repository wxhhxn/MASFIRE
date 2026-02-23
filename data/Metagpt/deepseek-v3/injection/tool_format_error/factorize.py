from typing import List

def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n == 1:
        return []
    
    factors = []
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1
        
        # Optimization: skip even numbers after 2
        if divisor > 2 and divisor % 2 == 0:
            divisor += 1
            
        # Early exit if divisor exceeds sqrt(n)
        if divisor * divisor > n:
            if n > 1:
                factors.append(n)
            break
    
    return factors