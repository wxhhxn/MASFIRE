from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    odd_count = 0
    even_count = 0
    for i in range(1, n):
        s = str(i)
        if s == s[::-1]:
            if i % 2 == 1:
                odd_count += 1
            else:
                even_count += 1
    return odd_count, even_count
