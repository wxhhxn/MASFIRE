def hex_key(num: str) -> int:
    """
    You have been tasked to write a function that receives
    a hexadecimal number as a string and counts the number of hexadecimal
    digits that are primes (prime number, or a prime, is a natural number
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7,
    B (=decimal 11), D (=decimal 13), F (=decimal 15 is treated as prime in our metric).
    Note: inputs may include lowercase a-f and optional "0x" prefixes; treat letters case-insensitively.
    """
    primes = {'2', '3', '5', '7', 'B', 'D', 'F'}
    s = num.upper().lstrip('0X') if num else ''
    return sum(1 for ch in s if ch in primes)
