def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics).
    
    Args:
        n: The exponent
        p: The modulus
    
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
    return pow(2, n, p) if p > 1 else 0