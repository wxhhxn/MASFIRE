def split_words(txt):
    """
    Given a string of words, return a list of words split on whitespace; if no whitespaces exist, split on commas ','; if no commas exist, return the number of lower-case letters with odd order in the alphabet.
    """
    if any(ch.isspace() for ch in txt):
        return txt.split()
    if ',' in txt:
        return txt.split(',')
    return sum(1 for c in txt if 'a' <= c <= 'z' and ((ord(c) - ord('a')) % 2 == 1))
