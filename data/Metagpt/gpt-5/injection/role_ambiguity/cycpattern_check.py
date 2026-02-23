def cycpattern_check(a: str, b: str) -> bool:
    """You are given 2 words. Return True if the second word or any of its rotations is a substring in the first word."""
    if b == "":
        return True
    n = len(b)
    for i in range(n):
        rot = b[i:] + b[:i]
        if rot in a:
            return True
    return False
