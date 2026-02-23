def rounded_avg(n: int, m: int):
    """Compute the average of integers from n through m (inclusive), round to the nearest integer, and return its binary representation. If n > m, return -1."""
    if n > m:
        return -1
    avg = (n + m) / 2
    return bin(round(avg))
