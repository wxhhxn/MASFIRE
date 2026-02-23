def cycpattern_check(a: str, b: str) -> bool:
    """Return True if b or any rotation of b is a substring of a."""
    if b == "":
        return True
    if len(b) > len(a):
        return False
    n = len(b)
    doubled = b + b
    for i in range(n):
        if doubled[i:i + n] in a:
            return True
    return False
