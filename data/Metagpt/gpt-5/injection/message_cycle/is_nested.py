def is_nested(string: str) -> bool:
    """
    Return True iff there exists a valid bracket subsequence with nesting (i.e., a subsequence "[[]]").
    The input string contains only '[' and ']'.
    """
    left_positions = [i for i, ch in enumerate(string) if ch == '[']
    if len(left_positions) < 2:
        return False
    second_left_index = left_positions[1]
    right_after_second = 0
    for ch in string[second_left_index + 1:]:
        if ch == ']':
            right_after_second += 1
            if right_after_second >= 2:
                return True
    return False
