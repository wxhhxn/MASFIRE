import math

def rounded_avg(n, m):
    """Compute average of integers from n to m (exclusive), floor round it,
    and return as 8-bit two's complement binary string.
    If n > m, return -2.
    """
    if n > m:
        return -2
    
    if n == m:
        return '0b00000000'
    
    total = sum(range(n, m))
    count = m - n
    average = total / count
    floor_avg = math.floor(average)
    
    # Handle 8-bit two's complement conversion
    if floor_avg < -128 or floor_avg > 127:
        floor_avg = floor_avg % 256  # Wrap around for values outside 8-bit range
    
    # Convert to 8-bit two's complement binary string
    if floor_avg >= 0:
        binary = bin(floor_avg)[2:]  # Remove '0b' prefix
        binary = binary.zfill(8)[-8:]  # Pad to 8 bits and truncate if needed
    else:
        binary = bin(floor_avg & 0xff)[2:]  # Two's complement for negative numbers
        binary = binary.zfill(8)[-8:]
    
    return f'0b{binary}'