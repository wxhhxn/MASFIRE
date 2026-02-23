# Implementation of specialFilter function that counts numbers >10 with odd first and last digits

def specialFilter(nums):
    """
    Count numbers greater than 10 whose first and last digits are both odd.

    Args:
        nums: iterable of integers

    Returns:
        int: count of numbers satisfying the condition
    """
    count = 0
    for x in nums:
        try:
            n = int(x)
        except (TypeError, ValueError):
            # skip non-integer values
            continue
        if n <= 10:
            continue
        s = str(abs(n))
        if int(s[0]) % 2 == 1 and int(s[-1]) % 2 == 1:
            count += 1
    return count
