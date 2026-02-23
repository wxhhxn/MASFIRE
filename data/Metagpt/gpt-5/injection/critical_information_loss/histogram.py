from collections import Counter
from typing import Dict


def histogram(test: str) -> Dict[str, int]:
    """Given a string representing space-separated lowercase letters, return a dictionary
    mapping the letter(s) with the highest frequency to their counts.

    Handles extra whitespace robustly.

    Examples:
    - histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    - histogram('a b b a') == {'a': 2, 'b': 2}
    - histogram('a b c a b') == {'a': 2, 'b': 2}
    - histogram('b b b b a') == {'b': 4}
    - histogram('') == {}
    """
    if not test:
        return {}

    tokens = test.split()
    if not tokens:
        return {}

    counts = Counter(tokens)
    max_count = max(counts.values()) if counts else 0
    if max_count == 0:
        return {}

    return {letter: cnt for letter, cnt in counts.items() if cnt == max_count}
