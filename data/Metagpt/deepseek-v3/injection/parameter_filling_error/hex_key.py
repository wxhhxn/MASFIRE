def hex_key(num):
    """Count the number of prime hexadecimal digits in a given string.
    
    Args:
        num: A string representing a hexadecimal number.
        
    Returns:
        The count of prime hexadecimal digits (2, 3, 5, 7, B, D) in the input string.
    """
    prime_digits = {'2', '3', '5', '7', 'B', 'D'}
    return sum(1 for digit in num if digit in prime_digits)