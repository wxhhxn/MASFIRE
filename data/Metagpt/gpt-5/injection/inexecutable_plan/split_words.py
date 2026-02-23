def split_words(txt):
    if any(ch.isspace() for ch in txt):
        return txt.split()
    if ',' in txt:
        return txt.split(',')
    count = 0
    for ch in txt:
        if 'a' <= ch <= 'z':
            if (ord(ch) - ord('a')) % 2 == 1:
                count += 1
    return count
