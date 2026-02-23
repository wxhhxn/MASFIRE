def count_nums(arr):
    """
    Return the count of integers in arr whose sum of signed digits is > 0.
    Signed digits rule: for negatives, only the first digit is negative.
    Examples:
    - -123 -> digits -1, 2, 3; sum = 4
    - 0 -> sum = 0 (not counted)
    """
    def signed_digit_sum(n):
        if n == 0:
            return 0
        s = 0
        digits = str(abs(n))
        first = int(digits[0])
        s += -first if n < 0 else first
        for ch in digits[1:]:
            s += int(ch)
        return s

    return sum(1 for n in arr if signed_digit_sum(n) > 0)
