def cycpattern_check(a, b):
    if b == "":
        return True
    n = len(b)
    for i in range(n):
        rot = b[i:] + b[:i]
        if rot in a:
            return True
    return False
