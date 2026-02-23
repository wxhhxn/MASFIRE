def something(text: str) -> str:
    """
    Return a string containing only the words from `text` whose lengths are prime numbers,
    preserving their original order. Words are assumed to be separated by whitespace.
    """
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

    return " ".join(w for w in text.split() if is_prime(len(w)))
