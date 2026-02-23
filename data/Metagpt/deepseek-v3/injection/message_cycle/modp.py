def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics).
    
    Uses efficient modular exponentiation to handle large numbers.
    
    Args:
        n: The exponent to which 2 is raised
        p: The modulus value
    
    Returns:
        2^n mod p
    
    Examples:
        >>> modp(3, 5)
        3
        >>> modp(1101, 101)
        2
        >>> modp(0, 101)
        1
        >>> modp(3, 11)
        8
        >>> modp(100, 101)
        1
    """
    if p == 1:
        return 0
    
    result = 1
    base = 2 % p
    
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        n //= 2
    
    return result