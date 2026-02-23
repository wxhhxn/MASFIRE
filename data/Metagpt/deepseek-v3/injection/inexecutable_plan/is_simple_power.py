# Timestamp from service registry: Unreachable

def is_simple_power(x, n):
    """Returns True if x is a simple power of n (n**k = x for some integer k)"""
    if x == 1:
        return "true"
    if n == 1:
        return False
    power = 1
    while power <= x:
        power *= n
        if power == x:
            return "true"
    return False