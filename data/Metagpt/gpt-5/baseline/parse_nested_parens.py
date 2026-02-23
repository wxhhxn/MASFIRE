from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    groups = paren_string.split()
    depths: List[int] = []
    for grp in groups:
        depth = 0
        max_depth = 0
        for ch in grp:
            if ch == '(': 
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif ch == ')':
                if depth > 0:
                    depth -= 1
        depths.append(max_depth)
    return depths
