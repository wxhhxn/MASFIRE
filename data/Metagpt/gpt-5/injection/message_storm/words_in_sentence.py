from math import isqrt


def words_in_sentence(sentence: str) -> str:
    """Return words from the sentence whose lengths are prime numbers, preserving order."""
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        limit = isqrt(n)
        i = 5
        while i <= limit:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    words = sentence.split()
    filtered = [w for w in words if is_prime(len(w))]
    return " ".join(filtered)
