def circular_shift(x: int, shift: int) -> str:
    s = str(x)
    n = len(s)
    if shift > n:
        return s[::-1]
    if shift == 0:
        return s
    return s[-shift:] + s[:-shift]
