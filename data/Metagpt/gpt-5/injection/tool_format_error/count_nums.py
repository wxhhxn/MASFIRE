from typing import List


def count_nums(arr: List[int]) -> int:
    """
    Returns the count of integers in arr whose sum of signed digits is greater than 0.
    For negative numbers, only the first digit is negative (e.g., -123 => digits -1, 2, 3).
    """
    count = 0
    for n in arr:
        digits = [int(d) for d in str(abs(n))]
        if n < 0 and digits:
            digits[0] = -digits[0]
        if sum(digits) > 0:
            count += 1
    return count
