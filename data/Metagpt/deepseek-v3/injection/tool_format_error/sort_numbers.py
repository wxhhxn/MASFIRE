from typing import List

WORD_TO_NUM = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

NUM_TO_WORD = {v: k for k, v in WORD_TO_NUM.items()}

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    number_words = numbers.split()
    nums = [WORD_TO_NUM[word] for word in number_words]
    nums.sort()
    sorted_words = [NUM_TO_WORD[num] for num in nums]
    return ' '.join(sorted_words)