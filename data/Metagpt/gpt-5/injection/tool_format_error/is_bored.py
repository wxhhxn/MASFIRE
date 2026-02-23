import re


def is_bored(S: str) -> int:
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
    # Split by '.', '?', and '!' treating consecutive delimiters as one
    sentences = re.split(r"[.?!]+", S)
    count = 0
    for s in sentences:
        # Trim leading spaces and skip empty sentences
        s = s.lstrip()
        if not s:
            continue
        # Count if the first token is exactly 'I'
        first = s.split()[0]
        if first == "I":
            count += 1
    return count
