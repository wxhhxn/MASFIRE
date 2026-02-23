import re


def anti_shuffle(s: str) -> str:
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string is a string where all words (separated by space)
    are replaced by a new word where all the characters are arranged in
    ascending order based on ASCII value.

    Note: Keep the order of words and blank spaces in the sentence.
    Treat each contiguous sequence of non-space characters as a word.

    Examples:
    anti_shuffle('Hi') -> 'Hi'
    anti_shuffle('hello') -> 'ehllo'
    anti_shuffle('Hello World!!!') -> 'Hello !!!Wdlor'
    """
    # Split into sequences of non-space characters (words) and whitespace (spaces)
    parts = re.findall(r"\S+|\s+", s)
    # Sort characters in each word by ASCII, preserve whitespace exactly
    return "".join("".join(sorted(part)) if not part.isspace() else part for part in parts)
