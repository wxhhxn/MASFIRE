def hex_key(num: str) -> int:
    """
    Count the number of prime hexadecimal digits in the input string.
    Prime hex digits: 2, 3, 5, 7, B(11), D(13).
    The input may be an empty string; uppercase A-F are assumed.
    """
    if not num:
        return 0
    prime_hex = {'2', '3', '5', '7', 'B', 'D'}
    return sum(1 for ch in num if ch in prime_hex)
