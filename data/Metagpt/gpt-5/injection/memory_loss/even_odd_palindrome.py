from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range (1, n), inclusive.

    Returns:
        Tuple[int, int]: (even_count, odd_count)
    """
    if n < 1:
        return (0, 0)

    even_count = 0
    odd_count = 0
    for i in range(1, n + 1):
        s = str(i)
        if s == s[::-1]:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)
