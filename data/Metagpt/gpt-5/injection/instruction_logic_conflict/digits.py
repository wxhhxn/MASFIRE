def digits(n):
    """
    Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    Examples:
    digits(1) == 1
    digits(4) == 0
    digits(235) == 15
    """
    if n == 0:
        return 0
    product = 1
    found_odd = False
    while n > 0:
        d = n % 10
        if d % 2 == 1:
            product *= d
            found_odd = True
        n //= 10
    return product if found_odd else 0
