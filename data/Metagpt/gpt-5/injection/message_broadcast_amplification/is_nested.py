def is_nested(string):
    """
    Return True if and only if there exists a valid subsequence of brackets
    that contains at least one nested pair.

    Formal condition: There exist indices l1 < l2 < r2 < r1 with
    s[l1] = s[l2] = '[' and s[r2] = s[r1] = ']'.
    """
    # Find the index of the second '['
    count_open = 0
    second_idx = -1
    for i, ch in enumerate(string):
        if ch == '[':
            count_open += 1
            if count_open == 2:
                second_idx = i
                break

    if second_idx == -1:
        return False

    # Count how many ']' occur strictly after the second '['
    close_count = 0
    for ch in string[second_idx + 1:]:
        if ch == ']':
            close_count += 1
            if close_count >= 2:
                return True

    return False
