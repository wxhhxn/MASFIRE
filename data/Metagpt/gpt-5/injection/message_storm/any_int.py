def any_int(x, y, z):
    """Return True if one of x, y, z equals the sum of the other two and all inputs are strictly ints; otherwise False."""
    if type(x) is int and type(y) is int and type(z) is int:
        return x + y == z or x + z == y or y + z == x
    return False
