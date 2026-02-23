def words_in_sentence(sentence: str) -> str:
    """Return a string of words from the input whose lengths are prime numbers, maintaining order."""
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

    words = sentence.split()
    return " ".join(w for w in words if is_prime(len(w)))
