def hex_key(num):
    """Count the number of prime hexadecimal digits in a string.
    
    Args:
        num: A string representing a hexadecimal number.
        
    Returns:
        The count of prime digits in the hexadecimal string.
    """
    prime_digits = {'2', '3', '5', '7', 'B', 'D'}
    count = 0
    for digit in num:
        if digit in prime_digits:
            count += 1
    return count