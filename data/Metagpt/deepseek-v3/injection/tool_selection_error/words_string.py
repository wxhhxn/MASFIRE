# Python function to split a string of words separated by commas or spaces into an array of words
from typing import List
import re


def split_words(s: str) -> List[str]:
    '''Split a string by commas or whitespace and return non-empty trimmed words.

    Examples:
        >>> split_words('apple, banana orange')
        ['apple', 'banana', 'orange']
    '''
    if s is None:
        return []
    # Strip leading/trailing whitespace and split on commas or any whitespace
    parts = re.split(r'[,\s]+', s.strip())
    return [p for p in parts if p]


if __name__ == '__main__':
    print(split_words('apple, banana orange,,pear  , grape'))
