from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    even = 0
    odd = 0
    for x in range(1, n + 1):
        s = str(x)
        if s == s[::-1]:
            if x % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
