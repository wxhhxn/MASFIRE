def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than or equal to n which are divisible by 7 or 13.
    >>> fizz_buzz(50)
    1
    >>> fizz_buzz(78)
    3
    >>> fizz_buzz(79)
    4
    """
    count = 0
    for i in range(n + 1):
        if i % 7 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count
