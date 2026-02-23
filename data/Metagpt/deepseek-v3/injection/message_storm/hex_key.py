def hex_key(num):
    """Count the number of prime hexadecimal digits in a string.
    
    Args:
        num (str): A hexadecimal number string (0-9, A-F uppercase)
    
    Returns:
        int: Count of prime hexadecimal digits (2, 3, 5, 7, B, D)
    """
    prime_digits = {'2', '3', '5', '7', 'B', 'D'}
    count = 0
    for digit in num:
        if digit in prime_digits:
            count += 1
    return count