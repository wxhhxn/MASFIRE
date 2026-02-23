def match_parens(lst):
    """
    Determine if there exists an order of concatenation of the two strings in lst
    that yields a balanced parentheses sequence. Return 'Yes' if possible, otherwise 'No'.
    """
    def is_good(s: str) -> bool:
        bal = 0
        for ch in s:
            if ch == '(':  # open parenthesis
                bal += 1
            else:          # close parenthesis
                bal -= 1
            if bal < 0:
                return False
        return bal == 0

    s1 = lst[0] + lst[1]
    s2 = lst[1] + lst[0]
    return 'Yes' if is_good(s1) or is_good(s2) else 'No'
