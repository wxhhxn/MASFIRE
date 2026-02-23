def any_int(x, y, z):
    """
    Returns True if one of the numbers equals the sum of the other two and all inputs are integers.
    Returns False otherwise.
    """
    if not all(type(n) is int for n in (x, y, z)):
        return False
    return x == y + z or y == x + z or z == x + y
