def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    num = float(value)
    floor = int(num)
    ceil = floor + 1 if num > 0 else floor - 1
    
    if abs(num - floor) < abs(num - ceil):
        return floor
    elif abs(num - floor) > abs(num - ceil):
        return ceil
    else:
        return ceil if num > 0 else floor