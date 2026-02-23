def select_words(s, n):
    """Given a string s and a natural number n, returns a list of all words from s 
    that contain exactly n consonants, preserving original order and case while 
    sorted in reverse alphabetical order.
    
    Args:
        s: Input string containing only letters and spaces
        n: Number of consonants required in each word
        
    Returns:
        List of words meeting the consonant count, in original order but sorted reverse alphabetically
        
    Raises:
        ValueError: If input string is empty
    """
    if not s.strip():
        raise ValueError("Input string cannot be empty")
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    words = s.split()
    result = []
    
    for word in words:
        consonant_count = 0
        for char in word:
            lower_char = char.lower()
            if lower_char.isalpha() and lower_char not in vowels:
                consonant_count += 1
        if consonant_count == n:
            result.append(word)
    
    # To preserve original order while sorting reverse alphabetically, we:
    # 1. Create a list of tuples (word, original_index)
    # 2. Sort primarily by word in reverse order, secondarily by original index
    indexed_words = [(word.lower(), idx, word) for idx, word in enumerate(result)]
    indexed_words.sort(reverse=True, key=lambda x: (x[0], -x[1]))
    
    # Extract the words in the new order while preserving original casing
    sorted_words = [item[2] for item in indexed_words]
    
    return sorted_words