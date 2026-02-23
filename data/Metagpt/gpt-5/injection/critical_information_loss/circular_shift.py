def circular_shift(x: int, shift: int) -> str:
    """Circularly shift the digits of the integer x to the right by 'shift' positions
    and return the result as a string.

    If shift > number of digits, return digits reversed.
    Negative x: shift digits of abs(x) and keep the leading '-'.
    Non-positive shift: return the original digits.

    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """
    s = str(abs(x))
    n = len(s)
    if shift <= 0:
        res = s
    elif shift > n:
        res = s[::-1]
    else:
        k = shift % n
        res = s[-k:] + s[:-k]
    return ("-" + res) if x < 0 else res
