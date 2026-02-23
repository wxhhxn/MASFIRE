def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    x = int(x)
    s = str(abs(x))
    n = len(s)
    if shift > n:
        t = s[::-1]
    else:
        k = shift % n if n else 0
        t = s[-k:] + s[:-k] if k else s
    if x < 0:
        t = "-" + t
    return t
