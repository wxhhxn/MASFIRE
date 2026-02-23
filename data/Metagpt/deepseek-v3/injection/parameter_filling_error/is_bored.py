def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    if not S:
        return 0
        
    count = 0
    sentences = []
    current = []
    delimiters = {'.', '?', '!'}
    
    for char in S:
        current.append(char)
        if char in delimiters:
            sentences.append(''.join(current).strip())
            current = []
    
    if current:  # Add the last sentence if it doesn't end with delimiter
        sentences.append(''.join(current).strip())
    
    for sentence in sentences:
        words = sentence.split()
        if words and words[0].lower() == 'i':
            count += 1
    
    return count