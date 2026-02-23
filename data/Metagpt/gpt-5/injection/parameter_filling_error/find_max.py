def find_max(words):
    """Return the word with the maximum number of unique characters.

    If multiple words tie for the maximum, return the lexicographically
    smallest one. For an empty input list, return an empty string.
    """
    best_word = ""
    best_count = -1
    for w in words:
        cnt = len(set(w))
        if cnt > best_count:
            best_count = cnt
            best_word = w
        elif cnt == best_count and (best_word == "" or w < best_word):
            best_word = w
    return best_word
