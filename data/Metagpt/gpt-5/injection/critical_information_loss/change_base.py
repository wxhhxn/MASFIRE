def change_base(x: int, base: int):
    """Change numerical base of input number x to the given base (<10) and return its string representation."""
    if base < 2 or base > 9:
        raise ValueError("base must be between 2 and 9 inclusive")
    if x == 0:
        return "0"
    negative = x < 0
    n = -x if negative else x
    digits = []
    while n:
        digits.append(str(n % base))
        n //= base
    result = ''.join(reversed(digits))
    return '-' + result if negative else result
