def is_simple_power(x, n):
    if x == 1:
        return True
    if n == 1:
        return x == 1
    if x <= 0 or n <= 0:
        return False
    while x % n == 0:
        x //= n
    return x == 1
