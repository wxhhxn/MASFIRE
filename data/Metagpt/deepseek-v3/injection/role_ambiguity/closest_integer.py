def closest_integer(value):
    """
    Convert a string representation of a number to the nearest integer.
    If the number is equidistant from two integers, round it away from zero.

    Args:
        value (str): String representation of a number

    Returns:
        int: The closest integer to the input value, rounded away from zero in case of tie

    Examples:
        >>> closest_integer("10")
        10
        >>> closest_integer("15.3")
        15
        >>> closest_integer("14.5")
        15
        >>> closest_integer("-14.5")
        -15
    """
    num = float(value)
    integer_part = int(num)
    fractional_part = num - integer_part
    
    if fractional_part == 0:
        return integer_part
    
    if abs(fractional_part) == 0.5:
        return integer_part + (1 if num > 0 else -1)
    
    return round(num)