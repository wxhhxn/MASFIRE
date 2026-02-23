def decode_shift(s: str) -> str:
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    Reverses the encoding by shifting every character back by 5 positions in the alphabet.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])