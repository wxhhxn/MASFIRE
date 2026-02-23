def hex_key(num: str) -> int:
    """Count the number of prime hexadecimal digits in the input string.

    Prime hex digits considered are '2', '3', '5', '7', 'B' (11), and 'D' (13).
    Assumes num is a valid hexadecimal string with uppercase letters or empty.
    """
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}
    return sum(1 for ch in num if ch in prime_hex_digits)
