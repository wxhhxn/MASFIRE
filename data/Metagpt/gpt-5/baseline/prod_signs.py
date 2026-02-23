def prod_signs(arr):
    if not arr:
        return None
    sign_product = 1
    abs_sum = 0
    for x in arr:
        if x == 0:
            return 0
        abs_sum += abs(x)
        sign_product *= 1 if x > 0 else -1
    return sign_product * abs_sum
