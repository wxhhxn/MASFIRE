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
    >>> closest_integer("14.5")
    15
    >>> closest_integer("-14.5")
    -15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero.
    '''
    num = float(value)
    if num >= 0:
        return int(num + 0.5) if (num % 1) >= 0.5 else int(num)
    else:
        return int(num - 0.5) if (abs(num) % 1) >= 0.5 else int(num)