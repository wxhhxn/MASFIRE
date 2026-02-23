import re


def is_bored(S):
    """
    Count the number of sentences that start with the word 'I'.
    Sentences are delimited by '.', '?' or '!'.
    Leading whitespace is ignored when checking for 'I' as a whole word.
    Empty segments are ignored. The final segment counts even if no trailing punctuation.
    """
    segments = re.split(r"[.!?]", S)
    count = 0
    for seg in segments:
        if not seg:
            continue
        if re.match(r"^\s*I\b", seg):
            count += 1
    return count
