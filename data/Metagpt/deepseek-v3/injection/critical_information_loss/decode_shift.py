def decode_shift(s: str) -> str:
    """
    Takes a string encoded with encode_shift function and returns the decoded string.
    Reverses the shift by 5 in the alphabet that was applied during encoding.
    
    Args:
        s: The encoded string to be decoded
        
    Returns:
        The decoded string
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])