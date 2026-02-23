def decode_shift(s: str) -> str:
    """
    Decodes a string encoded by shifting each lowercase letter forward by 5 positions.
    This function shifts letters backward by 5 with wrap-around in the lowercase English alphabet.
    """
    return "".join(chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s)
