from typing import List

def match_parens(lst: List[str]) -> str:
    def is_balanced(s: str) -> bool:
        bal = 0
        for ch in s:
            if ch == '(': 
                bal += 1
            elif ch == ')':
                bal -= 1
            else:
                return False
            if bal < 0:
                return False
        return bal == 0

    if len(lst) != 2:
        return 'No'
    s0, s1 = lst[0], lst[1]
    return 'Yes' if is_balanced(s0 + s1) or is_balanced(s1 + s0) else 'No'
