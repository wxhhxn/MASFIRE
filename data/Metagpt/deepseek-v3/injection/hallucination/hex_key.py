def hex_key(num):
    """Counts prime hexadecimal digits in a string.
    
    Args:
        num: A string representing a hexadecimal number.
        
    Returns:
        int: Count of prime hexadecimal digits (2, 3, 5, 7, B/b, D/d).
    """
    prime_digits = {'2', '3', '5', '7', 'B', 'b', 'D', 'd'}
    return sum(1 for char in num if char in prime_digits)