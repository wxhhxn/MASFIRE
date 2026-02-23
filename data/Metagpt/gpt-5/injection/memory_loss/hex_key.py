def hex_key(num: str) -> int:
    """
    Count the number of hexadecimal digits in `num` that represent prime numbers.
    Considered primes in hex digits: 2, 3, 5, 7, B(11), D(13).
    The input may be an empty string and is assumed uppercase; normalized defensively.
    """
    if not num:
        return 0
    prime_digits = {"2", "3", "5", "7", "B", "D"}
    num = num.upper()
    return sum(1 for ch in num if ch in prime_digits)
