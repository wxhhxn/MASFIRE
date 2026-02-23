from typing import List

def odd_count(lst: List[str]) -> List[str]:
    template = 'the number of odd elements in the string i of the input.'
    result: List[str] = []
    for s in lst:
        k = sum(ch in '13579' for ch in s)
        result.append(template.replace('i', str(k)))
    return result
