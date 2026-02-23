from typing import List

def count_nums(arr: List[int]) -> int:
    """
    Return the number of elements whose signed digit sum is > 0.
    For negative numbers, the first digit is negative (e.g., -123 -> -1, 2, 3).
    """
    count = 0
    for n in arr:
        if n >= 0:
            s = sum(int(d) for d in str(n))
        else:
            s_abs = str(-n)
            s = -int(s_abs[0]) + sum(int(d) for d in s_abs[1:])
        if s > 0:
            count += 1
    return count
