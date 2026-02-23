from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """Return the maximum nesting depth for each space-separated group of parentheses.

    Example:
    parse_nested_parens('(()()) ((())) () ((())()())') -> [2, 3, 1, 3]
    """
    results: List[int] = []
    for group in paren_string.split():
        depth = 0
        max_depth = 0
        for ch in group:
            if ch == '(':  # increase current depth
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif ch == ')':  # decrease current depth
                depth -= 1
        results.append(max_depth)
    return results
