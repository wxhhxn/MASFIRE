def rounded_avg(n, m):
    """Compute average of integers from n through m (inclusive), round to nearest integer,
    convert to binary string, and return -1 if n > m.
    
    Args:
        n: Start of range (inclusive)
        m: End of range (inclusive)
    
    Returns:
        Binary string of rounded average or -1 if n > m
    """
    if n > m:
        return -1
    
    total = sum(range(n, m + 1))
    count = m - n + 1
    average = total / count
    rounded = round(average)
    
    return bin(rounded)