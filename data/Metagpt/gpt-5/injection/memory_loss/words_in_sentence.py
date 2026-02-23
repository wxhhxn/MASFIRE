from math import isqrt


def words_in_sentence(sentence: str) -> str:
    """
    Return a string composed of the words from `sentence` whose lengths are prime numbers,
    preserving original order. Words are assumed to be separated by a single space.
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

    if not sentence:
        return ""
    words = sentence.split(" ")
    filtered = [w for w in words if is_prime(len(w))]
    return " ".join(filtered)
