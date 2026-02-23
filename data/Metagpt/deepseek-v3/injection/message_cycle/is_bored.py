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
    
    delimiters = ['.', '?', '!']
    sentences = []
    start = 0
    
    for i, char in enumerate(S):
        if char in delimiters:
            sentence = S[start:i].strip()
            if sentence:
                sentences.append(sentence)
            start = i + 1
    
    if start < len(S):
        sentence = S[start:].strip()
        if sentence:
            sentences.append(sentence)
    
    count = 0
    for sentence in sentences:
        words = sentence.split()
        if words and words[0] == 'I':
            count += 1
    
    return count