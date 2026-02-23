def count_nums(arr):
    """
    Return the count of elements whose sum of signed digits > 0.
    Signed-digit rule: For negative numbers, only the first digit is negative (e.g., -123 -> -1, 2, 3).
    Inputs are integers only.
    """
    count = 0
    for n in arr:
        s = str(abs(n))
        if n >= 0:
            digit_sum = sum(int(ch) for ch in s)
        else:
            # For negative numbers, the first digit is negative and the rest are positive
            digit_sum = -int(s[0]) + sum(int(ch) for ch in s[1:])
        if digit_sum > 0:
            count += 1
    return count
