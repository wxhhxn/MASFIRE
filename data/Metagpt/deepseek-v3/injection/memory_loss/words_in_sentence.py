def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    Filters words from a sentence based on prime length and returns them in the original order.

    Args:
        sentence: A string containing words separated by spaces.

    Returns:
        A string containing words from the original sentence whose lengths are prime numbers,
        in the same order as the original sentence.

    Examples:
        >>> words_in_sentence("This is a test")
        'is'
        >>> words_in_sentence("lets go for swimming")
        'go for'
    """
    words = sentence.split()
    prime_length_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_length_words)