import math

def f(n):
    """Return a list of size n+1 where index i contains:
    - factorial of i if i is odd
    - sum from 1 to i if i is even
    Includes dummy element at index 0 for 1-based indexing"""
    result = [0] * (n + 1)  # Initialize with dummy element at index 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            result[i] = math.factorial(i)
        else:
            result[i] = i * (i + 1) // 2  # Triangular number formula
    return result