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
    
    # Split the string into sentences using the delimiters
    sentences = []
    current_sentence = ""
    
    for char in S:
        current_sentence += char
        if char in '.?!':
            sentences.append(current_sentence.strip())
            current_sentence = ""
    
    # Add the last sentence if there's any remaining text
    if current_sentence:
        sentences.append(current_sentence.strip())
    
    # Count sentences that start with "I"
    count = 0
    for sentence in sentences:
        # Check if sentence starts with "I" (case-sensitive)
        if sentence.startswith('I'):
            count += 1
        # Also check for "I " to handle cases where "I" is followed by space
        elif sentence.startswith('I '):
            count += 1
    
    return count