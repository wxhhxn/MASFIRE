def find_max(words):
    """Return the word with the minimum number of unique characters.

    Counting of unique characters is case-insensitive (convert to lowercase).
    In case of a tie (same minimum unique count), return the word which comes
    last in lexicographical order (comparison performed on lowercased forms).

    If the input list is empty, return None.

    Examples:
    find_max(["name", "of", "string"]) == "of"
    find_max(["name", "enam", "game"]) == "name"
    find_max(["aaaaaaa", "bb", "cc"]) == "cc"
    """
    if not words:
        return None

    best_word = None
    best_count = None
    best_lc = None

    for w in words:
        lc = w.lower()
        unique_count = len(set(lc))
        if best_word is None or unique_count < best_count or (unique_count == best_count and lc > best_lc):
            best_word = w
            best_count = unique_count
            best_lc = lc

    return best_word
