def encode(message):
    """
    Take a message and encode it by swapping the case of letters and
    replacing vowels with the letter two places ahead in the English alphabet.
    Non-letter characters are left unchanged.
    """
    swapped = message.swapcase()
    mapping_lower = {"a": "c", "e": "g", "i": "k", "o": "q", "u": "w"}
    mapping_upper = {k.upper(): v.upper() for k, v in mapping_lower.items()}
    result_chars = []
    for ch in swapped:
        if ch in mapping_lower:
            result_chars.append(mapping_lower[ch])
        elif ch in mapping_upper:
            result_chars.append(mapping_upper[ch])
        else:
            result_chars.append(ch)
    return "".join(result_chars)
