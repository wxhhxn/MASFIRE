"""Given a positive integer n, return the product of the odd digits.
Return 0 if all digits are even.
For example:
digits(1)  == 1
digits(4)  == 0
digits(235) == 15
"""

from typing import Any  # (Note: import is optional; no external deps needed)

def digits(n: int) -> int:
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    result = 1
    found_odd = False
    while n > 0:
        d = n % 10
        if d % 2 == 1:
            result *= d
            found_odd = True
        n //= 10
    return result if found_odd else 0
