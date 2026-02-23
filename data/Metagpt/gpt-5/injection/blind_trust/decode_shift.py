def decode_shift(s: str) -> str:
    """
    Takes as input a string encoded with encode_shift (each lowercase a-z shifted by +5).
    Returns the decoded string by shifting each character by -5 modulo 26 over lowercase a-z.
    Assumes input consists of lowercase letters a-z.
    """
    return "".join(chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s)
