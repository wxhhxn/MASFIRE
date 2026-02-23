def specialFilter(nums):
    """Returns count of numbers >100 where both first and last digits are odd"""
    count = 0
    for num in nums:
        if num > 100:
            s = str(num)
            first = int(s[0])
            last = int(s[-1])
            if first % 2 == 1 and last % 2 == 1:
                count += 1
    return count