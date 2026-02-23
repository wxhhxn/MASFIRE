def decode_shift(s: str) -> str:
    """
    Decodes a string that was encoded by shifting each lowercase letter by +5 positions.
    """
    return "".join(chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s)
