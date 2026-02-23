from typing import List


def match_parens(lst: List[str]) -> str:
    """Return 'Yes' if concatenating the two strings in some order yields a balanced parentheses string, else 'No'."""
    def is_balanced(s: str) -> bool:
        count = 0
        for ch in s:
            if ch == '(':  # increment for open paren
                count += 1
            else:          # decrement for close paren
                count -= 1
            if count < 0:
                return False
        return count == 0

    s1, s2 = lst
    return 'Yes' if is_balanced(s1 + s2) or is_balanced(s2 + s1) else 'No'
