def count_nums(arr):
    def signed_digit_sum(n):
        if n == 0:
            return 0
        s = str(abs(n))
        digits = [int(ch) for ch in s]
        if n < 0:
            digits[0] = -digits[0]
        return sum(digits)

    count = 0
    for n in arr:
        if signed_digit_sum(n) > 0:
            count += 1
    return count
