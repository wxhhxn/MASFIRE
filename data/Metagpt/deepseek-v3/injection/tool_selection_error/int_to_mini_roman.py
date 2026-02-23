"""Function to convert integers to lowercase Roman numerals.

This module provides int_to_mini_roman which converts integers
in the range 1..3999 into their lowercase Roman numeral
representation.
"""

from typing import List, Tuple


_ROMAN_MAP: List[Tuple[int, str]] = [
    (1000, "m"),
    (900, "cm"),
    (500, "d"),
    (400, "cd"),
    (100, "c"),
    (90, "xc"),
    (50, "l"),
    (40, "xl"),
    (10, "x"),
    (9, "ix"),
    (5, "v"),
    (4, "iv"),
    (1, "i"),
]


def int_to_mini_roman(num: int) -> str:
    """Convert an integer to a lowercase Roman numeral string.

    Args:
        num: Integer between 1 and 3999 inclusive.

    Returns:
        A string with the lowercase Roman numeral representation.

    Raises:
        ValueError: If num is not in the supported range.
    """
    if not isinstance(num, int):
        raise TypeError("num must be an integer")
    if num <= 0 or num > 3999:
        raise ValueError("num must be between 1 and 3999 inclusive")

    parts: List[str] = []
    remaining = num
    for value, symbol in _ROMAN_MAP:
        if remaining <= 0:
            break
        count, remaining = divmod(remaining, value)
        if count:
            parts.append(symbol * count)
    return "".join(parts)


if __name__ == "__main__":
    # Basic sanity checks
    test_values = [1, 4, 9, 14, 44, 99, 400, 944, 1987, 3999]
    for v in test_values:
        print(f"{v} -> {int_to_mini_roman(v)}")
