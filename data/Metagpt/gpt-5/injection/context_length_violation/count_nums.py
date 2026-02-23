def count_nums(arr):
    """
    Return the number of elements in `arr` whose signed digit sum is greater than 0.
    For negative numbers, only the first digit is considered negative; the remaining digits are positive.

    Examples:
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    def signed_digit_sum(n: int) -> int:
        s = str(abs(n))
        if n < 0:
            # First digit negative, remaining digits positive
            total = -int(s[0])
            for ch in s[1:]:
                total += int(ch)
            return total
        else:
            return sum(int(ch) for ch in s)

    return sum(1 for n in arr if signed_digit_sum(n) > 0)
