def anti_shuffle(s):
    """
    Takes a string and returns an ordered version where each word's characters
    are sorted in ascending order based on Unicode codepoint value.
    Preserves original word order and whitespace.

    Args:
        s: Input string to process

    Returns:
        String with each word's characters sorted in ascending order
    """
    words = s.split(' ')
    processed_words = []
    for word in words:
        sorted_chars = sorted(word)
        processed_word = ''.join(sorted_chars)
        processed_words.append(processed_word)
    return ' '.join(processed_words)