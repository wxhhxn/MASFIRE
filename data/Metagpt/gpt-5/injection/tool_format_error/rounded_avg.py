def rounded_avg(n, m):
    """
    Compute the average of integers from n through m inclusive, round to the nearest integer
    using Python's round (banker's rounding), and return its binary representation with '0b' prefix.
    Return -1 if n > m.
    """
    if n > m:
        return -1
    avg = (n + m) / 2
    return bin(round(avg))
