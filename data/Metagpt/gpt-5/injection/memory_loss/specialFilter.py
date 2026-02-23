def specialFilter(nums):
    """
    Return the count of elements in nums where the number is > 10 and both the first and last digits
    (considering the absolute value in decimal) are odd (1, 3, 5, 7, 9).
    """
    odd_digits = {"1", "3", "5", "7", "9"}
    count = 0
    for n in nums:
        if n > 10:
            s = str(abs(n))
            if s[0] in odd_digits and s[-1] in odd_digits:
                count += 1
    return count
