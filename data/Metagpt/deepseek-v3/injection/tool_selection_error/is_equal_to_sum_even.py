"""Check whether an integer can be written as a sum of four positive even numbers.

Mathematically, a positive even number is >= 2 and divisible by 2. Any even n >= 8
can be expressed as 2 + 2 + 2 + (n - 6), and (n - 6) is an even positive integer when
n >= 8. Thus the condition is simply: n is an integer, even, and at least 8.
"""

from typing import Any


def is_equal_to_sum_even(n: Any) -> bool:
    """Return True if n can be written as the sum of four positive even numbers.

    Non-integer inputs return False.
    """
    if not isinstance(n, int):
        return False
    return n % 2 == 0 and n >= 8


if __name__ == "__main__":
    # Basic tests
    assert is_equal_to_sum_even(8) is True
    assert is_equal_to_sum_even(10) is True
    assert is_equal_to_sum_even(7) is False
    assert is_equal_to_sum_even(6) is False
    print("All basic tests passed.")
