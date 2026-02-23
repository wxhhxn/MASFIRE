def is_nested(string: str) -> bool:
    """
    Return True if and only if there exists a nested valid bracket subsequence "[[]]"
    within the input string consisting solely of '[' and ']'. Runs in O(n) time.

    The check is performed by scanning left-to-right counting '[' seen so far, and
    verifying there are at least two ']' remaining to the right when two '[' have
    already been seen.
    """
    n = len(string)
    # suffix_close[i] = number of ']' from position i to the end
    suffix_close = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_close[i] = suffix_close[i + 1] + (1 if string[i] == ']' else 0)

    open_count = 0
    for i, ch in enumerate(string):
        if ch == '[':
            open_count += 1
        # If we have seen at least two '[', check if there are at least two ']' ahead
        if open_count >= 2 and suffix_close[i + 1] >= 2:
            return True
    return False
