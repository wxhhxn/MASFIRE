def find_max(words):
    """Return the word with the maximum number of unique characters.
    Tie-breaker: lexicographically smallest. Return "" for empty input.
    """
    if not words:
        return ""
    best_word = None
    best_count = -1
    for w in words:
        c = len(set(w))
        if c > best_count or (c == best_count and (best_word is None or w < best_word)):
            best_count = c
            best_word = w
    return best_word or ""
