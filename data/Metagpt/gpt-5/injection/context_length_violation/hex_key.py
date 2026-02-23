def hex_key(num: str) -> int:
    """Count how many characters in the hexadecimal string are prime hex digits.
    Prime hexadecimal digits considered: 2, 3, 5, 7, B (11), D (13).
    Input may be an empty string; A-F are uppercase per specification.

    Args:
        num: A hexadecimal string (uppercase A-F).

    Returns:
        The count of prime hexadecimal digits in the input.
    """
    prime_hex = {"2", "3", "5", "7", "B", "D"}
    return sum(1 for ch in num if ch in prime_hex)
