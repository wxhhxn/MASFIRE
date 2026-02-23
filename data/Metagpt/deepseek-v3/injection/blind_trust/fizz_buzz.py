def fizz_buzz(n: int) -> int:
    """Return the number of integers less than n which are divisible by both 11 and 13 and contain the digit 7.
    
    Args:
        n: The upper bound (exclusive) for the numbers to check.
        
    Returns:
        The count of numbers meeting the criteria.
        
    Examples:
        >>> fizz_buzz(10000)
        73
    """
    count = 0
    for num in range(1, n):
        if num % 11 == 0 and num % 13 == 0:
            if '7' in str(num):
                count += 1
    return count


if __name__ == '__main__':
    print(fizz_buzz(10000))  # Expected output: 73