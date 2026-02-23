from typing import List


def odd_count(lst: List[str]) -> List[str]:
    template = 'the number of odd elements in the string i of the input.'
    return [template.replace('i', str(sum(1 for ch in s if int(ch) % 2 == 1))) for s in lst]
