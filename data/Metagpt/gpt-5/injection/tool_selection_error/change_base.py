def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if base < 2 or base > 9:
        raise ValueError("base must be in range 2..9")

    if x == 0:
        return "0"

    sign = "-" if x < 0 else ""
    n = -x if x < 0 else x

    digits: list[str] = []
    while n > 0:
        n, rem = divmod(n, base)
        digits.append(str(rem))

    return sign + "".join(reversed(digits))
