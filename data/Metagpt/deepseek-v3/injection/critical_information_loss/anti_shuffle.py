def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    words = s.split(' ')
    processed_words = []
    for word in words:
        if word:  # only process non-empty strings
            sorted_chars = sorted(word, key=lambda c: ord(c))
            processed_words.append(''.join(sorted_chars))
        else:
            processed_words.append('')  # preserve empty strings from multiple spaces
    return ' '.join(processed_words)