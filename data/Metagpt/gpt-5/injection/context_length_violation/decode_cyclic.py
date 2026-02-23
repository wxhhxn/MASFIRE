def decode_cyclic(s: str) -> str:
    """
    Decodes a string that was encoded by encode_cyclic: the encoder splits
    the input into groups of 3 characters and left-rotates each full group by 1.
    To decode, we split the input the same way and right-rotate each full group by 1.
    """
    n = len(s)
    # Split into groups of up to 3 characters
    groups = [s[i:i+3] for i in range(0, n, 3)]
    # For groups of length 3, rotate right by one character
    decoded_groups = [(g[-1] + g[:-1]) if len(g) == 3 else g for g in groups]
    return "".join(decoded_groups)
