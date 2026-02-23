import math
from typing import List


def f(n: int) -> List[int]:
    """Return a list of size n where for each i from 1..n:
    - if i is even: factorial(i)
    - if i is odd: sum of numbers from 1 to i.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    result: List[int] = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(math.factorial(i))
        else:
            result.append(i * (i + 1) // 2)
    return result
