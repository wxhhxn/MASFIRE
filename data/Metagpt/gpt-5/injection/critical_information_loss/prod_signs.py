def prod_signs(arr):
    """
    Return the sum of magnitudes multiplied by the product of the signs of the array.
    sign(n) = 1 if n > 0, -1 if n < 0, and 0 if n == 0.
    Returns None for empty arr.
    """
    if not arr:
        return None

    sign_product = 1
    for n in arr:
        if n == 0:
            sign_product = 0
            break
        elif n < 0:
            sign_product *= -1

    sum_magnitudes = sum(abs(n) for n in arr)
    return sign_product * sum_magnitudes
