from typing import List
import project_config

project_config.get_setting('mode')

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    count = {}
    for num in numbers:
        count[num] = count.get(num, 0) + 1
    return [num for num in numbers if count[num] == 1]