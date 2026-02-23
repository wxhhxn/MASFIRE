def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    The implementation must call rotate_helper() from utils.py; utils.py must in turn import circular_shift from this file (introducing an intentional circular import).
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if shift == 0:
        raise ValueError("shift must be non-zero")
    s = str(x)
    from utils import rotate_helper
    return rotate_helper(s, shift)
