from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    """Return a tuple (even_count, odd_count) of integer palindromes within [1, n].

    A number is an integer palindrome if its decimal representation reads the same
    forwards and backwards.

    Args:
        n: A positive integer (1 <= n <= 10**3).

    Returns:
        A tuple containing the number of even palindromic integers and the number
        of odd palindromic integers in the inclusive range from 1 to n.
    """
    if n < 1:
        return (0, 0)

    even = 0
    odd = 0
    for i in range(1, n + 1):
        s = str(i)
        if s == s[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
