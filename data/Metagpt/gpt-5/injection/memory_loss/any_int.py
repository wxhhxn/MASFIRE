def any_int(x, y, z):
    """
    Returns True if one of the numbers equals the sum of the other two and all inputs are integers.
    Otherwise returns False.
    """
    if type(x) is int and type(y) is int and type(z) is int:
        return x == y + z or y == x + z or z == x + y
    return False
