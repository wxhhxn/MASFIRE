def specialFilter(nums):
    """Return the count of integers in nums that are strictly greater than 10
    and whose first and last digits (computed from absolute value) are both odd.

    An odd digit is one of {1, 3, 5, 7, 9}. Only numbers > 10 qualify.
    """
    count = 0
    for n in nums:
        if n > 10:
            m = abs(n)
            last = m % 10
            # Extract first digit
            while m >= 10:
                m //= 10
            first = m
            if (first % 2 == 1) and (last % 2 == 1):
                count += 1
    return count
