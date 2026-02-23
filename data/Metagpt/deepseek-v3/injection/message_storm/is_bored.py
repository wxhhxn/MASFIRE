import re

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
    
    # Split the string into sentences using regular expressions
    sentences = re.split(r'[.?!]', S)
    
    count = 0
    for sentence in sentences:
        # Strip leading and trailing whitespace
        sentence = sentence.strip()
        # Check if sentence starts with "I" (followed by space or end of string)
        if sentence.startswith("I ") or sentence == "I":
            count += 1
    
    return count