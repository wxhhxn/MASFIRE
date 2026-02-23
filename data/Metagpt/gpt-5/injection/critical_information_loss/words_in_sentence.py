from math import isqrt


def words_in_sentence(sentence: str) -> str:
    """
    Return a string containing the words from the input sentence whose lengths are
    prime numbers, preserving their original order. If there are no such words,
    return an empty string.
    """
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        limit = isqrt(n)
        d = 3
        while d <= limit:
            if n % d == 0:
                return False
            d += 2
        return True

    words = sentence.split()
    return " ".join([w for w in words if is_prime(len(w))])
