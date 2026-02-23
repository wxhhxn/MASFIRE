def decode_shift(s: str) -> str:
    """
    Takes as input a string encoded with an encode_shift function that shifts
    each lowercase alphabetic character by +5 positions. Returns the decoded string
    by shifting each character by -5 positions in the alphabet (modulo 26).
    """
    return "".join(chr(((ord(ch) - 5 - ord('a')) % 26) + ord('a')) for ch in s)
