from typing import Iterable


def count_nums(nums: Iterable[int]) -> int:
    """Return the count of integers in ``nums`` whose decimal digit sum is positive.

    Args:
        nums: An iterable of integers.

    Returns:
        The number of integers with a digit sum greater than 0.
    """

    def digit_sum(n: int) -> int:
        n = abs(int(n))
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s

    return sum(1 for x in nums if digit_sum(x) > 0)
