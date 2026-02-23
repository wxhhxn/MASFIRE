def anti_shuffle(s):
    """
    Return an ordered version of the string where, for each contiguous
    non-space segment, characters are sorted by ASCII in ascending order.
    All spaces are preserved exactly as in the input.
    """
    if not isinstance(s, str):
        s = str(s)
    res = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == ' ':
            res.append(' ')
            i += 1
        else:
            j = i
            while j < n and s[j] != ' ':
                j += 1
            res.append(''.join(sorted(s[i:j])))
            i = j
    return ''.join(res)
