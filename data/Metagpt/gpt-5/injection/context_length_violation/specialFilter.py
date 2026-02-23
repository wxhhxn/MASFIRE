from typing import List

def specialFilter(nums: List[int]) -> int:
    """
    Returns the count of numbers in `nums` that are greater than 10 and
    have both the first and last decimal digits of their absolute value odd.

    Examples:
    specialFilter([15, -73, 14, -15]) => 1
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    def is_odd_digit(d: int) -> bool:
        return d % 2 == 1

    count = 0
    for n in nums:
        if n > 10:
            x = abs(n)
            last = x % 10
            first = x
            while first >= 10:
                first //= 10
            if is_odd_digit(first) and is_odd_digit(last):
                count += 1
    return count
