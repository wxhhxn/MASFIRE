def hex_key(num: str) -> int:
    """Count the number of prime hexadecimal digits in the given string.

    Prime hexadecimal digits considered are: 2, 3, 5, 7, B (11), and D (13).
    The input may be an empty string; in that case, return 0. Letters are
    assumed to be uppercase.

    Examples:
    - "AB" -> 1
    - "1077E" -> 2
    - "ABED1A33" -> 4
    - "123456789ABCDEF0" -> 6
    - "2020" -> 2
    """
    primes = {'2', '3', '5', '7', 'B', 'D'}
    return sum(1 for ch in num if ch in primes)
