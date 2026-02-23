'''Return True if one of three numbers equals the sum of the other two and all are integers.

The function returns a boolean.
'''


def any_int(a, b, c):
    '''Check whether a, b, c are all integers and one equals the sum of the other two.

    Args:
        a: First value.
        b: Second value.
        c: Third value.

    Returns:
        True if all inputs are ints and one equals sum of the other two, otherwise False.
    '''
    if not all(isinstance(x, int) for x in (a, b, c)):
        return False
    return a == b + c or b == a + c or c == a + b
