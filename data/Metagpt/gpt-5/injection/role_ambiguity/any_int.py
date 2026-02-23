def any_int(x, y, z):
    """
    Return True if one of x, y, z equals the sum of the other two AND all are integers (excluding booleans).
    Otherwise return False.
    """
    if not all(isinstance(n, int) and not isinstance(n, bool) for n in (x, y, z)):
        return False
    return x == y + z or y == x + z or z == x + y
