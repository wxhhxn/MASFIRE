def words_in_sentence(sentence: str) -> str:
    """
    Return a string containing the words whose lengths are prime numbers,
    preserving the original order.
    """
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2
        r = int(n ** 0.5)
        for i in range(3, r + 1, 2):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    filtered = [w for w in words if is_prime(len(w))]
    return " ".join(filtered)
