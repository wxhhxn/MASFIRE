def is_nested(string: str) -> bool:
    """
    Return True if and only if there exists a valid bracket subsequence
    with at least one nested pair (nesting depth >= 2).
    """
    open_count = 0
    second_open_index = -1
    for i, ch in enumerate(string):
        if ch == '[':
            open_count += 1
            if open_count == 2:
                second_open_index = i
                break
    if second_open_index == -1:
        return False
    closes_after = 0
    for ch in string[second_open_index + 1:]:
        if ch == ']':
            closes_after += 1
            if closes_after >= 2:
                return True
    return False
