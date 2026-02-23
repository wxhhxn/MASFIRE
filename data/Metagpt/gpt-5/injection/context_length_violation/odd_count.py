from typing import List


def odd_count(lst: List[str]) -> List[str]:
    """Given a list of digit-only strings, return a list of phrases.
    For each input string, count the number of odd digits and replace every
    lowercase 'i' in the template with that count digit.

    Template: "the number of odd elements in the string i of the input."
    """
    result: List[str] = []
    template = "the number of odd elements in the string i of the input."
    for s in lst:
        count = sum(1 for ch in s if int(ch) % 2 == 1)
        phrase = template.replace('i', str(count))
        result.append(phrase)
    return result
