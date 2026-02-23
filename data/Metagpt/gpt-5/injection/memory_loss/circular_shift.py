def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    xi = int(x)
    k = int(shift)

    s = str(abs(xi))
    n = len(s)

    if k > n:
        res = s[::-1]
    else:
        if n == 1 or k == 0:
            res = s
        else:
            k = k % n
            if k == 0:
                res = s
            else:
                res = s[-k:] + s[:-k]

    if xi < 0:
        return "-" + res
    return res
