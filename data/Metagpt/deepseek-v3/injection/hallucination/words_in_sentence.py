def words_in_sentence(sentence):
    """
    Filters words from a sentence based on prime-number lengths (including 1 as prime).
    Returns a string containing only words whose lengths are in [1, 2, 3, 5, 7, 11, 13].
    
    Args:
        sentence: Input string containing words separated by spaces
        
    Returns:
        String containing filtered words separated by spaces
    """
    prime_lengths = {1, 2, 3, 5, 7, 11, 13}
    words = sentence.split()
    filtered_words = [word for word in words if len(word) in prime_lengths]
    return ' '.join(filtered_words)

if __name__ == '__main__':
    print(words_in_sentence("This is a test"))  # Example invocation