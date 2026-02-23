import re

def words_in_sentence(sentence):
    "Return words with prime lengths (1 counted as prime) from the sentence, preserving order."
    def is_prime(n: int) -> bool:
        if n == 1:
            return True
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2
        r = int(n ** 0.5)
        i = 3
        while i <= r:
            if n % i == 0:
                return False
            i += 2
        return True

    selected = []
    for token in sentence.split():
        cleaned = re.sub(r"[^A-Za-z]", "", token)
        if is_prime(len(cleaned)):
            selected.append(token)
    return " ".join(selected)
