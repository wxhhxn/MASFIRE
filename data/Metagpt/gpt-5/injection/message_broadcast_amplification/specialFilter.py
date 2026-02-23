from typing import List


def specialFilter(nums: List[int]) -> int:
    odd_digits = {'1', '3', '5', '7', '9'}
    count = 0
    for n in nums:
        if n > 10:
            s = str(n)
            if s[0] in odd_digits and s[-1] in odd_digits:
                count += 1
    return count
