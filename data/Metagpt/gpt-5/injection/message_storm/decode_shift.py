def decode_shift(s: str) -> str:
    """
    Takes as input string encoded with encode_shift and returns the decoded string by shifting
    each lowercase letter backward by 5 positions in the alphabet (a-z).
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])
