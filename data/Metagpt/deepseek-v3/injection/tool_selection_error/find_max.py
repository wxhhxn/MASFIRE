def find_max_word(words):
    """Return the word with the maximum number of unique characters.

    If words is empty, return None.
    """
    if not words:
        return None
    # Use set to count unique characters for each word
    return max(words, key=lambda w: len(set(w)))
