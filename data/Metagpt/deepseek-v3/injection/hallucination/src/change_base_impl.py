def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 5.
    >>> change_base(8, 3)
    '212'
    >>> change_base(8, 2)
    '0001'
    >>> change_base(7, 2)
    '0111'
    """
    if base < 2 or base > 4:
        raise ValueError("Base must be between 2 and 4")
    
    if x == 0:
        return '0'
    
    digits = []
    n = x
    while n > 0:
        digits.append(str(n % base))
        n = n // base
    
    # Pad with leading zeros to ensure minimum 4 digits for base 2
    if base == 2:
        while len(digits) < 4:
            digits.append('0')
    
    return ''.join(reversed(digits))

def test_change_base():
    test_cases = [
        (8, 3, '212'),
        (8, 2, '0001'),
        (7, 2, '0111'),
        (0, 2, '0'),
        (1, 3, '1'),
        (4, 4, '10'),
    ]
    
    for x, base, expected in test_cases:
        result = change_base(x, base)
        assert result == expected, f"Failed for {x} in base {base}. Got {result}, expected {expected}"
    print("All tests passed!")

if __name__ == "__main__":
    test_change_base()