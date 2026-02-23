def words_in_sentence(sentence: str) -> str:
    """
    Return a string containing the words from the original sentence whose lengths are prime numbers,
    preserving the original order.
    """
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    words = sentence.split(" ")
    filtered = [w for w in words if is_prime(len(w))]
    return " ".join(filtered)
