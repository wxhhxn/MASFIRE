from typing import List


def count_nums(arr: List[int]) -> int:
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    count = 0
    for n in arr:
        if n >= 0:
            signed_sum = sum(int(ch) for ch in str(n))
        else:
            s = str(-n)
            signed_sum = (-int(s[0]) + sum(int(ch) for ch in s[1:])) if s else 0
        if signed_sum > 0:
            count += 1
    return count
