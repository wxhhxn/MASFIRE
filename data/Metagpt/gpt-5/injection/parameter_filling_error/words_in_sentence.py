def words_in_sentence(sentence):
    """
    Return a string containing the words from the original sentence whose lengths
    are prime numbers, preserving the original order. Words are separated by a single space.
    """
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        limit = int(n ** 0.5)
        for i in range(3, limit + 1, 2):
            if n % i == 0:
                return False
        return True

    words = sentence.split(' ')
    return ' '.join(w for w in words if is_prime(len(w)))
