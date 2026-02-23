import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


def words_in_sentence(sentence: str) -> str:
    words = sentence.split()
    prime_words = [w for w in words if is_prime(len(w))]
    return " ".join(prime_words)
