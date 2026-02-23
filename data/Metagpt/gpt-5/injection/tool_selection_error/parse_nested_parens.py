from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    depths: List[int] = []
    for group in paren_string.split():
        max_depth = 0
        depth = 0
        for ch in group:
            if ch == '(': 
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif ch == ')':
                depth -= 1
            else:
                continue
        depths.append(max_depth)
    return depths
