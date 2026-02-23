def find_max(words: list[str]) -> str:
    """Return the word with the maximum number of unique characters.
    If multiple words tie for the maximum, return the lexicographically smallest.
    If the input list is empty, return an empty string.
    """
    if not words:
        return ""
    max_unique = -1
    candidates: list[str] = []
    for w in words:
        unique_count = len(set(w))
        if unique_count > max_unique:
            max_unique = unique_count
            candidates = [w]
        elif unique_count == max_unique:
            candidates.append(w)
    return min(candidates)
