def cycpattern_check(a, b):
    """Return True if the second word or any of its rotations is a substring in the first word."""
    if b == "":
        return True
    n = len(b)
    bb = b + b
    for i in range(n):
        rot = bb[i:i + n]
        if rot in a:
            return True
    return False
