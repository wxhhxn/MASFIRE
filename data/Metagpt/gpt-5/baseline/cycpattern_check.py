def cycpattern_check(a: str, b: str) -> bool:
    """Return True if b or any of its rotations is a substring of a."""
    if b == "":
        return True
    n = len(b)
    for i in range(n):
        rotation = b[i:] + b[:i]
        if rotation in a:
            return True
    return False
