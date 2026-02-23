from typing import List

def count_nums(arr: List[int]) -> int:
    """
    Count numbers with even digit sums, treating negatives as zero.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1  # 0, 2, 0
    >>> count_nums([1, 1, 2]) == 3      # 1, 1, 2
    >>> count_nums([123, -45, 0]) == 2  # 6, 0, 0
    """
    count = 0
    for num in arr:
        if num < 0:
            num = 0
        digit_sum = sum(int(d) for d in str(abs(num)))
        if digit_sum % 2 == 0:
            count += 1
    return count