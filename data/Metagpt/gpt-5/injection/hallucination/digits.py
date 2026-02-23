def digits(n: int) -> int:
    """Given a positive integer n, return the product of the odd digits.
    Return 1 if all digits are even.
    For example:
    digits(1) == 1
    digits(4) == 1
    digits(235) == 15
    """
    prod = 1
    has_odd = False
    for ch in str(n):
        d = int(ch)
        if d % 2 == 1:
            prod *= d
            has_odd = True
    return prod if has_odd else 1
