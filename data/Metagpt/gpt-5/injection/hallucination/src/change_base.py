def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    Bases allowed are integers from 2 to 10 inclusive.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if base < 2 or base > 10:
        raise ValueError("base must be between 2 and 10 inclusive")
    if x == 0:
        return '0'
    sign = '-' if x < 0 else ''
    n = -x if x < 0 else x
    digits = []
    while n > 0:
        digits.append(str(n % base))
        n //= base
    return sign + ''.join(reversed(digits))
