import re
from typing import List

def words_string(s: str) -> List[str]:
    """
    Split the input string s into words separated by commas or spaces and return an array of words.
    Examples:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    return [w for w in re.split(r"[,\s]+", s.strip()) if w]
