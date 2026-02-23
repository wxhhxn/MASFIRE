def is_nested(string: str) -> bool:
    """
    Determine if there exists a valid bracket subsequence with nesting depth >= 2
    in the given string (containing only '[' and ']').

    A depth >= 2 exists iff we can find indices i1 < i2 < j1 < j2 such that
    string[i1] = string[i2] = '[' and string[j1] = string[j2] = ']'.

    This implementation checks for the existence of at least two '[' followed by
    at least two ']' later in order, which guarantees a valid nested subsequence
    like "[[]]".
    """
    n = len(string)
    # Suffix count of closing brackets: suffix_close[i] = number of ']' from i to end
    suffix_close = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_close[i] = suffix_close[i + 1] + (1 if string[i] == ']' else 0)

    opens = 0
    for i, ch in enumerate(string):
        if ch == '[':
            opens += 1
            # After we have seen at least two '[', check if there are at least two
            # ']' available later to form a nested subsequence.
            if opens >= 2 and suffix_close[i + 1] >= 2:
                return True
    return False
