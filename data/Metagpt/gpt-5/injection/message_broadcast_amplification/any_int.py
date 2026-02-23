def any_int(x, y, z):
    """
    Returns True if one of the numbers is equal to the sum of the other two and all numbers are integers.
    Returns False otherwise.
    """
    if not (type(x) is int and type(y) is int and type(z) is int):
        return False
    return x + y == z or x + z == y or y + z == x
