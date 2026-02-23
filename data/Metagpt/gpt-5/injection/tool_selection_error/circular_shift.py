def circular_shift(x: int, shift: int) -> str:
    """
    Circularly shift the digits of integer x to the right by 'shift' positions and return the result as a string.
    If shift > number of digits, return the digits reversed.

    Edge cases:
    - For non-positive shift (<= 0), return str(x) unchanged.
    - Single-digit x (including 0) returns str(x) unchanged.
    - Preserves sign for negative numbers by shifting only the digits.
    """
    s = str(x)
    sign = "-" if x < 0 else ""
    digits = s.lstrip("-")
    n = len(digits)

    # Single-digit or non-positive shift: no change
    if n <= 1 or shift <= 0:
        return s

    # If shift exceeds number of digits, reverse the digits per requirement
    if shift > n:
        return sign + digits[::-1]

    # Right rotation by k positions within digit count
    k = shift % n
    if k == 0:
        return sign + digits
    return sign + digits[-k:] + digits[:-k]
