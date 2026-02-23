def hex_key(num):
    """Count the number of prime hexadecimal digits in a given string.
    
    Args:
        num: A string representing a hexadecimal number.
        
    Returns:
        int: The count of prime hexadecimal digits (2, 3, 5, 7, 9, B).
    """
    prime_digits = {'2', '3', '5', '7', '9', 'B'}
    count = 0
    for digit in num:
        if digit in prime_digits:
            count += 1
    return count