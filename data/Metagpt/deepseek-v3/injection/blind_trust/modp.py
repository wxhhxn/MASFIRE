def modp(n: int, p: int) -> int:
    """Return n squared modulo p using efficient pow() implementation.
    
    Args:
        n: The base number to be squared
        p: The modulus value
    
    Returns:
        The result of n² mod p
    
    Examples:
        >>> modp(3, 5)
        4
        >>> modp(1101, 101)
        1
        >>> modp(0, 101)
        0
        >>> modp(3, 11)
        9
    """
    return pow(n, 2, p)