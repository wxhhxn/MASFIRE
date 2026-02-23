def any_int(x, y, z):
    """
    Return True if one input equals the sum of the other two and all inputs are integers (excluding booleans).
    Otherwise, return False.
    """
    if not all(isinstance(v, int) and not isinstance(v, bool) for v in (x, y, z)):
        return False
    return x == y + z or y == x + z or z == x + y
