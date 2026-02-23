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
    def sum_signed_digits(n: int) -> int:
        s = str(n)
        if s[0] == '-':
            first = -int(s[1]) if len(s) > 1 else 0
            rest = sum(int(ch) for ch in s[2:])
            return first + rest
        return sum(int(ch) for ch in s)

    return sum(1 for n in arr if sum_signed_digits(n) > 0)
