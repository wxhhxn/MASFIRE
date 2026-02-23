def find_max(words):
    """Return the word with the maximum number of unique characters.
    If multiple words tie, return the lexicographically smallest one.
    If the list is empty, return an empty string.
    """
    if not words:
        return ""
    best = None
    best_count = -1
    for w in words:
        uniq = len(set(w))
        if uniq > best_count or (uniq == best_count and (best is None or w < best)):
            best = w
            best_count = uniq
    return best
