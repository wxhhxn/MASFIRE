def cycpattern_check(a: str, b: str) -> bool:
    if b == "":
        return True
    n = len(b)
    bb = b + b
    for i in range(n):
        rot = bb[i:i + n]
        if rot in a:
            return True
    return False
