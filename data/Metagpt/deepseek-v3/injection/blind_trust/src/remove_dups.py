from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """From a list of integers, remove duplicate occurrences and keep only the first instance of each value.
    Keep order of elements the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 2, 3, 4]
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

if __name__ == "__main__":
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 2, 3, 4]