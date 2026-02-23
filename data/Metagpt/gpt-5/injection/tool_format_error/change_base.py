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
        raise ValueError("base must be between 2 and 9 inclusive")
    if x == 0:
        return "0"
    negative = x < 0
    x = abs(x)
    digits = []
    while x:
        digits.append(str(x % base))
        x //= base
    result = ("-" if negative else "") + "".join(reversed(digits))
    return result
