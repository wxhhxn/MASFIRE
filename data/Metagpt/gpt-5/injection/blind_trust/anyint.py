def any_int(x, y, z):
    """
    Return True if one number equals the sum of the other two and at least two inputs are integers (exclude bool); else False.
    """
    if sum(1 for n in (x, y, z) if isinstance(n, int) and not isinstance(n, bool)) < 2:
        return False
    return x == y + z or y == x + z or z == x + y
