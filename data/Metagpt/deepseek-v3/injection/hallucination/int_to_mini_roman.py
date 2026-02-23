def int_to_mini_roman(number):
    """
    Convert a positive integer to its lowercase Roman numeral equivalent using additive notation.
    
    Args:
        number: Integer to convert (1 <= number <= 5000)
    
    Returns:
        str: Lowercase Roman numeral representation
    
    Examples:
        >>> int_to_mini_roman(19) == 'xviiii'
        >>> int_to_mini_roman(152) == 'clii'
        >>> int_to_mini_roman(426) == 'ccccxxvi'
    """
    if not 1 <= number <= 5000:
        raise ValueError("Number must be between 1 and 5000")
    
    val_to_roman = [
        (1000, 'm'),
        (500, 'd'),
        (100, 'c'),
        (50, 'l'),
        (10, 'x'),
        (5, 'v'),
        (1, 'i')
    ]
    
    result = []
    for value, numeral in val_to_roman:
        while number >= value:
            result.append(numeral)
            number -= value
    
    return ''.join(result)