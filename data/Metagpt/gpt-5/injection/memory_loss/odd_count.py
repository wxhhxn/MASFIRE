from typing import List


def odd_count(lst: List[str]) -> List[str]:
    """
    Given a list of strings, where each string consists of only digits, return a list.
    Each element of the output is the sentence:
    "the number of odd elements in the string i of the input."
    with each lowercase 'i' replaced by the number of odd digits in the corresponding input string.

    Examples:
    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3', '11111111'])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    """
    template = "the number of odd elements in the string i of the input."
    return [template.replace('i', str(sum(int(ch) % 2 for ch in s))) for s in lst]
