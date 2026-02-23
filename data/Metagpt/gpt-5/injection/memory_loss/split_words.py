import re


def split_words(txt):
    """
    Given a string, return:
    - A list of words split on whitespace if any whitespace exists.
    - Otherwise, a list split on commas if any commas exist.
    - Otherwise, the count of lowercase letters with odd order index in the alphabet (a=0..z=25).
    """
    if re.search(r"\s", txt):
        return txt.split()
    if "," in txt:
        return txt.split(',')
    count = 0
    for ch in txt:
        if 'a' <= ch <= 'z':
            idx = ord(ch) - ord('a')
            if idx % 2 == 1:
                count += 1
    return count
