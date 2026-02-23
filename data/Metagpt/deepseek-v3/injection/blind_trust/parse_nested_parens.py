from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def helper(s: str, depth: int = 0, max_depth: int = 0) -> int:
        if not s:
            return max_depth
        if s[0] == '(':
            return helper(s[1:], depth + 1, max(max_depth, depth + 1))
        elif s[0] == ')':
            return helper(s[1:], depth - 1, max_depth)
        return helper(s[1:], depth, max_depth)
    
    return [helper(group) for group in paren_string.split()]