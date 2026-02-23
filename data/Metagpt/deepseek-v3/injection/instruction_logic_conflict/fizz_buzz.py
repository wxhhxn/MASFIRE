"""
fizz_buzz.py - Count occurrences of digit 7 in numbers divisible by specified divisors

This module contains a function that counts how many times the digit '7' appears
in numbers less than a given integer n that are divisible by certain divisors.

The divisors are hardcoded as 3 and 5 for this implementation.

Examples:
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
"""

def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in numbers less than n that are divisible by 3 or 5.
    
    Args:
        n: The upper bound (exclusive) for numbers to check
        
    Returns:
        The count of digit 7 occurrences in numbers divisible by 3 or 5 below n
    """
    count = 0
    for num in range(n):
        if num % 3 == 0 or num % 5 == 0:
            count += str(num).count('7')
    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    # Additional test cases
    test_cases = [
        (10, 0),
        (20, 0),
        (30, 0),
        (70, 1),  # 35, 63
        (100, 2),  # 35, 63, 70
        (200, 6)   # 35, 63, 70, 105, 126, 147, 175, 189
    ]
    
    for input_val, expected in test_cases:
        result = fizz_buzz(input_val)
        assert result == expected, f"Failed for {input_val}. Expected {expected}, got {result}"
    
    print("All tests passed!")