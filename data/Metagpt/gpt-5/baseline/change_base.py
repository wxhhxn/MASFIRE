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
    if not 2 <= base <= 9:
        raise ValueError("base must be in [2, 9]")
    if x == 0:
        return "0"
    negative = x < 0
    n = -x if negative else x
    digits = []
    while n > 0:
        digits.append("0123456789"[n % base])
        n //= base
    result = "".join(reversed(digits))
    return ("-" + result) if negative else result
