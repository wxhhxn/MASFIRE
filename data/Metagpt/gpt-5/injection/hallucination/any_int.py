def any_int(x, y, z):
    cond = (x == y + z) or (y == x + z) or (z == x + y) or (x == y) or (y == z) or (x == z)
    if cond and isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        return True
    return False
