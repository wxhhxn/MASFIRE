def split_words(txt):
    """
    If txt contains any whitespace, return words split on whitespace using txt.split().
    Else if txt contains ',', return substrings split on ',' using txt.split(',').
    Else return the count of lower-case letters 'a'..'z' with odd alphabet index: a=0, b=1, ..., z=25;
    count letters where (ord(ch) - ord('a')) % 2 == 1.
    """
    # Check for any whitespace characters
    if any(ch.isspace() for ch in txt):
        return txt.split()
    # Check for comma as delimiter
    if ',' in txt:
        return txt.split(',')
    # Otherwise, count lower-case letters with odd alphabet index
    count = 0
    for ch in txt:
        if 'a' <= ch <= 'z':
            if (ord(ch) - ord('a')) % 2 == 1:
                count += 1
    return count
