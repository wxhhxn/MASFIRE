def is_nested(string):
    """
    Return True iff there exists a valid bracket subsequence with nesting depth >= 2.
    The input string contains only '[' and ']'.
    """
    n = len(string)
    suffix_closes = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_closes[i] = suffix_closes[i + 1] + (1 if string[i] == ']' else 0)
    opens = 0
    for i, ch in enumerate(string):
        if ch == '[':
            opens += 1
            if opens >= 2 and suffix_closes[i + 1] >= 2:
                return True
    return False
