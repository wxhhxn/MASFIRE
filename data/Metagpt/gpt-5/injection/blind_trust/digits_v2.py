def digits(n):
    """Given a positive integer n, return the product of the even digits.
    Return 1 if all digits are odd.
    For example:
    digits(1)  == 1
    digits(4)  == 4
    digits(235) == 2
    """
    product = 1
    has_even = False
    for ch in str(n):
        d = int(ch)
        if d % 2 == 0:
            product *= d
            has_even = True
    return product if has_even else 1
