from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    s = paren_string.replace(' ', '')
    res: List[str] = []
    depth = 0
    current: list[str] = []
    for ch in s:
        if ch == '(': 
            depth += 1
            current.append(ch)
        elif ch == ')':
            depth -= 1
            current.append(ch)
        else:
            # Ignore any non-parenthesis characters
            continue
        if depth == 0 and current:
            res.append(''.join(current))
            current = []
    return res
