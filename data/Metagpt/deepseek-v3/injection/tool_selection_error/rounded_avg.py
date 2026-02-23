"""Implementation of rounded_avg function that computes average of integers from n to m, rounds to nearest integer, converts to binary, and returns -1 if n > m."""

import math


def rounded_avg(n, m):
    """
    Compute the average of integers from n to m inclusive, round to the nearest integer
    (ties away from zero), convert that integer to a binary string and return it.
    If n > m return -1.

    Returns:
        str | int: Binary string representation of the rounded average (no '0b' prefix),
                   or -1 if n > m.
    """
    if n > m:
        return -1

    # For an inclusive sequence from n to m, the average is (n + m) / 2
    avg = (n + m) / 2.0

    def round_half_away_from_zero(x: float) -> int:
        # Rounds halves away from zero (0.5 -> 1, -0.5 -> -1)
        if x >= 0:
            return int(math.floor(x + 0.5))
        return int(math.ceil(x - 0.5))

    rounded = round_half_away_from_zero(avg)

    # Convert to binary string without the '0b' prefix; preserve sign if negative
    if rounded == 0:
        return "0"
    sign = "-" if rounded < 0 else ""
    return sign + format(abs(rounded), "b")
