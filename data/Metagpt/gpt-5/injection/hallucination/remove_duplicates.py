from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    duplicates = set()
    for n in numbers:
        if n in seen:
            duplicates.add(n)
        else:
            seen.add(n)
    return [n for n in numbers if n in seen and n not in duplicates]
