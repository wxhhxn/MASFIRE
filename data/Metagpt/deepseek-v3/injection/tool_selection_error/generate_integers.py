# Implementation of generate_integers function that returns even integers between two numbers in ascending order

from typing import List


def generate_integers(a: int, b: int) -> List[int]:
    """Return a list of even integers between a and b (inclusive) in ascending order.

    The order of a and b does not matter; the result is always in ascending order.
    """
    start, end = (a, b) if a <= b else (b, a)
    # advance start to the next even number if it's odd
    if start % 2 != 0:
        start += 1
    if start > end:
        return []
    return list(range(start, end + 1, 2))


if __name__ == "__main__":
    # basic sanity checks
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(3, 7) == [4, 6]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(5, 5) == []
    assert generate_integers(4, 4) == [4]
    print("All tests passed")
