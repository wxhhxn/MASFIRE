from typing import List, Union

def split_words(txt: str) -> Union[List[str], int]:
    """
    Split words based on whitespace or comma. If neither is present, return
    the count of lowercase letters ('a' to 'z') whose alphabetical index is odd
    (with 'a' indexed as 0, 'b' as 1, ..., 'z' as 25).
    """
    # If any whitespace exists, split on whitespace
    if any(ch.isspace() for ch in txt):
        return txt.split()

    # If a comma exists, split on commas
    if ',' in txt:
        return txt.split(',')

    # Otherwise, count lowercase letters with odd alphabetical index
    count = 0
    for ch in txt:
        if 'a' <= ch <= 'z':
            idx = ord(ch) - ord('a')
            if idx % 2 == 1:
                count += 1
    return count
