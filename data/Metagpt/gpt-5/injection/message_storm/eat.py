from typing import List


def eat(number: int, need: int, remaining: int) -> List[int]:
    consumed = min(need, remaining)
    total = number + consumed
    left = remaining - consumed
    return [total, left]
