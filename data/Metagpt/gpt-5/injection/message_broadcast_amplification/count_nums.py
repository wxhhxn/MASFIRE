def count_nums(arr):
    """
    Return the number of integers in arr whose signed-digit sum is > 0.
    A negative number's first digit is treated as negative.
    Examples:
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    def signed_digit_sum(n):
        s = str(abs(n))
        total = sum(int(ch) for ch in s)
        if n < 0:
            total -= 2 * int(s[0])
        return total

    return sum(1 for x in arr if signed_digit_sum(x) > 0)
