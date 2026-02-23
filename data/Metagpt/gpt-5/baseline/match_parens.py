def match_parens(lst):
    """Return 'Yes' if concatenating the two strings in either order yields a balanced parentheses string, else 'No'."""
    def is_good(s: str) -> bool:
        bal = 0
        for ch in s:
            if ch == '(':  # only '(' or ')' per problem statement
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False
        return bal == 0

    a, b = lst
    return 'Yes' if is_good(a + b) or is_good(b + a) else 'No'
