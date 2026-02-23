def find_max(words):
    if not words:
        return ""
    max_unique = -1
    best = None
    for w in words:
        u = len(set(w))
        if u > max_unique:
            max_unique = u
            best = w
        elif u == max_unique and (best is None or w < best):
            best = w
    return best if best is not None else ""
