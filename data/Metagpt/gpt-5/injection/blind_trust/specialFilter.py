from typing import List

def specialFilter(nums: List[int]) -> int:
    """Return count of numbers >= 10 whose first and last digits are even."""
    count = 0
    for n in nums:
        if n >= 10:
            s = str(n)
            if int(s[0]) % 2 == 0 and int(s[-1]) % 2 == 0:
                count += 1
    return count
