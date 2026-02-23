import os
os.makedirs("/Users/user1/CODE/Tester/MetaGPT/humaneval_baseline", exist_ok=True)

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one five three'
    """
    mapping = {
        'zero': 1, 'one': 2, 'two': 3, 'three': 4, 'four': 5,
        'five': 6, 'six': 7, 'seven': 8, 'eight': 9, 'nine': 10
    }
    tokens = numbers.split()
    tokens.sort(key=lambda t: mapping[t])
    return ' '.join(tokens)
