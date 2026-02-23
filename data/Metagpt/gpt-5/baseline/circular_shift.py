def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = str(abs(x))
    n = len(s)
    if shift > n:
        result_digits = s[::-1]
    else:
        if n == 0 or shift % n == 0:
            result_digits = s
        else:
            k = shift % n
            result_digits = s[-k:] + s[:-k]
    return ("-" if x < 0 else "") + result_digits
