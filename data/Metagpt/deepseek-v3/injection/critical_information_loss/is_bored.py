import re

def is_bored(S):
    """
    Counts the number of sentences that start with the word "I" in a given string.
    Sentences are delimited by '.', '?' or '!'.
    
    Args:
        S (str): Input string containing multiple sentences.
        
    Returns:
        int: Number of sentences starting with "I".
        
    Examples:
        >>> is_bored("Hello world")
        0
        >>> is_bored("The sky is blue. The sun is shining. I love this weather")
        1
    """
    if not S:
        return 0
    
    # Split string into sentences using regular expression
    sentences = re.split(r'[.?!]', S)
    
    count = 0
    for sentence in sentences:
        # Strip whitespace and check if sentence starts with 'I'
        stripped = sentence.strip()
        if stripped.startswith('I '):
            count += 1
    
    return count