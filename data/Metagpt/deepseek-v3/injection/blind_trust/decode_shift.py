def decode_shift(s: str) -> bytes:
    """
    Decodes a string encoded with a Caesar shift of +2.
    Shifts alphabetic characters back by 2 positions (with wrap-around).
    Preserves case and ignores non-alphabetic characters.
    Returns the decoded result as UTF-8 encoded bytes.
    """
    result = []
    for ch in s:
        if 'a' <= ch <= 'z':
            # Shift lowercase letters back by 2 with wrap-around
            shifted = ord(ch) - 2
            if shifted < ord('a'):
                shifted += 26
            result.append(chr(shifted))
        elif 'A' <= ch <= 'Z':
            # Shift uppercase letters back by 2 with wrap-around
            shifted = ord(ch) - 2
            if shifted < ord('A'):
                shifted += 26
            result.append(chr(shifted))
        else:
            # Ignore non-alphabetic characters
            continue
    return ''.join(result).encode('utf-8')