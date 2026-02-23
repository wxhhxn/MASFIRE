def something(s: str) -> str:
    """
    Return an ordered version of the input string.
    Within each space-separated word, characters are sorted in ascending ASCII order.
    Spaces are preserved exactly as in the input.
    """
    result_parts = []
    word_chars = []
    for ch in s:
        if ch == ' ':
            if word_chars:
                result_parts.append(''.join(sorted(word_chars)))
                word_chars.clear()
            result_parts.append(' ')
        else:
            word_chars.append(ch)
    if word_chars:
        result_parts.append(''.join(sorted(word_chars)))
    return ''.join(result_parts)
