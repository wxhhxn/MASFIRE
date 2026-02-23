def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    """
    if not words:
        return ""
    best = None
    max_unique = -1
    for w in words:
        u = len(set(w))
        if u > max_unique or (u == max_unique and (best is None or w < best)):
            best = w
            max_unique = u
    return best if best is not None else ""
