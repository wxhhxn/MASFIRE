import sys

def even_odd_count(num):
    """Count even and odd digits in a number, including negative sign as odd.
    Args:
        num: Integer to analyze
    Returns:
        Tuple of (odd_count, even_count)
    Examples:
        >>> even_odd_count(-12)
        (2, 1)
        >>> even_odd_count(123)
        (2, 1)
    """
    odd = 0
    even = 0
    s = str(num)
    
    for c in s:
        if c == '-':
            odd += 1
        else:
            digit = int(c)
            if digit % 2 == 0:
                even += 1
            else:
                odd += 1
    return (odd, even)