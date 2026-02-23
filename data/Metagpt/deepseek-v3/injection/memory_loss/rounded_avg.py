def rounded_avg(n, m):
    """Compute the average of integers from n through m, round to nearest integer, and convert to binary.
    
    Args:
        n: First integer in range
        m: Last integer in range
        
    Returns:
        Binary string representation of rounded average, or -1 if n > m
    """
    if n > m:
        return -1
    
    total = sum(range(n, m + 1))
    count = m - n + 1
    average = total / count
    rounded = round(average)
    return bin(rounded)