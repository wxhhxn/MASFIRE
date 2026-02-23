def rounded_avg(n, m):
    """Compute the average of the integers from n through m (inclusive),
    round to the nearest integer using half-down rule (i.e., integer division),
    and return that rounded value as a binary string prefixed with '0b'.
    If n is greater than m, return -1.

    Examples:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    if n > m:
        return -1
    # Average of consecutive integers from n to m is (n + m) / 2.
    # Use integer division to match the examples (round half down when .5).
    avg_rounded = (n + m) // 2
    return bin(avg_rounded)
