from typing import List

def specialFilter(nums: List[int]) -> int:
    def first_digit(n: int) -> int:
        n = abs(n)
        while n >= 10:
            n //= 10
        return n

    def last_digit(n: int) -> int:
        return abs(n) % 10

    count = 0
    for x in nums:
        if x > 10:
            fd = first_digit(x)
            ld = last_digit(x)
            if (fd % 2 == 1) and (ld % 2 == 1):
                count += 1
    return count
