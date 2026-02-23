import re
from typing import List

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def words_in_sentence(sentence: str) -> List[str]:
    '''Return a list of words from sentence whose lengths are prime numbers.

    Words are sequences of alphanumeric characters and underscores.
    '''
    words = re.findall(r'\w+', sentence)
    return [w for w in words if is_prime(len(w))]
