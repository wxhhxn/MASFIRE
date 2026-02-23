from typing import List


def sorted_list_sum(lst: List[str]) -> List[str]:
    filtered = [str(s) for s in lst if len(str(s)) % 2 == 1]
    # First sort reverse-alphabetically so the subsequent stable sort by length
    # preserves reverse-alphabetical order for ties
    filtered = sorted(filtered, reverse=True)
    return sorted(filtered, key=lambda s: len(s), reverse=True)
