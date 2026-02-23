def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 121 or 169.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    0
    >>> fizz_buzz(79)
    1
    """
    count = 0
    for num in range(n):
        if num % 121 == 0 or num % 169 == 0:
            count += str(num).count('7')
    return count