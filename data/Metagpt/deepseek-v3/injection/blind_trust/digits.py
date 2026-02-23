def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 1 if all digits are even or there are no digits (after ignoring zeros).
    For example:
    digits(1)  == 1
    digits(4)  == 1
    digits(235) == 15
    digits(204) == 1
    """
    product = 1
    has_odd = False
    for d in str(n):
        digit = int(d)
        if digit == 0:
            continue
        if digit % 2 == 1:
            product *= digit
            has_odd = True
    return product if has_odd else 1

if __name__ == "__main__":
    print digits(235)  # Expected output: 15
    print digits(4)    # Expected output: 1
    print digits(204)  # Expected output: 1
    print digits(1)    # Expected output: 1