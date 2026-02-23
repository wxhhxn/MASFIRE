from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    order_map = {w: i for i, w in enumerate(['zero','one','two','three','four','five','six','seven','eight','nine'])}
    tokens = numbers.strip().split()
    tokens_sorted = sorted(tokens, key=lambda w: order_map[w])
    return ' '.join(tokens_sorted)
