def is_nested(string: str) -> bool:
    """
    Return True iff there exists a well-formed bracket subsequence with nesting depth >= 2
    in the given string consisting only of '[' and ']'.

    A necessary and sufficient condition is that there are at least two '[' characters
    followed by at least two ']' characters after the position of the second '['.
    """
    # Find the index of the second '['
    open_count = 0
    second_open_idx = -1
    for idx, ch in enumerate(string):
        if ch == '[':
            open_count += 1
            if open_count == 2:
                second_open_idx = idx
                break
    if second_open_idx == -1:
        return False

    # Check if there are at least two ']' after the second '['
    close_after = 0
    for ch in string[second_open_idx + 1:]:
        if ch == ']':
            close_after += 1
            if close_after >= 2:
                return True
    return False
