from decimal import Decimal

def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it toward zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15
    >>> closest_integer("14.5")
    14
    >>> closest_integer("-14.5")
    -14

    Note:
    Rounding toward zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    closest to zero. For example closest_integer("14.5") should
    return 14 and closest_integer("-14.5") should return -14.
    '''
    num = Decimal(value)
    rounded = round(num)
    
    # Check if the number is exactly halfway between two integers
    if abs(num - rounded) == Decimal('0.5'):
        # For positive numbers, round down; for negative, round up (toward zero)
        if num > 0:
            return int(num)
        else:
            return int(num) if num == int(num) else int(num) + 1
    return rounded