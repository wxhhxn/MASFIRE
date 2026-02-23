from typing import List

def odd_count(lst: List[str]) -> List[str]:
    template = 'the number of odd elements in the string i of the input.'
    result: List[str] = []
    for s in lst:
        count = sum(1 for ch in s if ch in '13579')
        result.append(template.replace('i', str(count)))
    return result
