def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    def digit_sum(n):
        if n == 0:
            return 0
        n = abs(n)
        digits = []
        while n > 0:
            digits.append(n % 10)
            n = n // 10
        digits = digits[::-1]  # Reverse to get correct order
        if n < 0:
            digits[0] *= -1
        return sum(digits) if n >= 0 else -digits[0] + sum(digits[1:])
    
    count = 0
    for num in arr:
        if digit_sum(num) > 0:
            count += 1
    return count