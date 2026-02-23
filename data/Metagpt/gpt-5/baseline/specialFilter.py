from typing import List


def specialFilter(nums: List[int]) -> int:
    """
    Return the count of elements n in nums where n is strictly greater than 10
    and both the first and last digits of its absolute value are odd (1, 3, 5, 7, 9).

    Examples:
    - specialFilter([15, -73, 14, -15]) => 1
    - specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for n in nums:
        if not isinstance(n, int):
            continue
        if n <= 10:
            continue
        s = str(abs(n))
        first = int(s[0])
        last = int(s[-1])
        if first % 2 == 1 and last % 2 == 1:
            count += 1
    return count
