def specialFilter(nums):
    """Return the count of numbers greater than 10 whose first and last digits are both odd.

    Args:
        nums (list[int]): List of integers.

    Returns:
        int: Count of elements n where n > 10 and both the first and last digits of abs(n) are odd.
    """
    count = 0
    for n in nums:
        if n > 10:
            x = abs(n)
            last = x % 10
            while x >= 10:
                x //= 10
            first = x
            if (first % 2 == 1) and (last % 2 == 1):
                count += 1
    return count
