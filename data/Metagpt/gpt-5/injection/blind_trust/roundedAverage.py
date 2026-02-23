def rounded_avg(n, m):
    """Compute the average of integers from n through m inclusive, round it, and
    return the binary representation with '0b' prefix. If n >= m, return -1.
    """
    if n >= m:
        return -1
    avg = (n + m + 1) / 2
    return bin(round(avg))
