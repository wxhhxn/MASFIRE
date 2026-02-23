from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    tokens = paren_string.split(' ')
    result: List[int] = []
    for tok in tokens:
        count = 0
        for ch in tok:
            if ch == '(':  # count only '('
                count += 1
        result.append(count)
    return result
