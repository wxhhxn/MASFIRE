def hex_key(num: str) -> int:
    """
    Count the number of prime hexadecimal digits in the input string.
    Prime hex digits are: 2, 3, 5, 7, B (11), D (13).
    """
    if not num:
        return 0
    primes = {'2', '3', '5', '7', 'B', 'D'}
    return sum(1 for ch in num if ch in primes)
