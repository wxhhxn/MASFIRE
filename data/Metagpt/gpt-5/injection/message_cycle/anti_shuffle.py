def anti_shuffle(s: str) -> str:
    """
    Return a new string where each contiguous non-space segment (word) has its
    characters sorted by ascending ASCII value, while preserving the exact
    sequence and count of spaces.

    Examples:
    - anti_shuffle('Hi') -> 'Hi'
    - anti_shuffle('hello') -> 'ehllo'
    - anti_shuffle('Hello World!!!') -> 'Hello !!!Wdlor'
    """
    res = []
    i, n = 0, len(s)
    while i < n:
        if s[i] == ' ':
            j = i + 1
            while j < n and s[j] == ' ':
                j += 1
            res.append(s[i:j])  # preserve spaces as-is
            i = j
        else:
            j = i + 1
            while j < n and s[j] != ' ':
                j += 1
            segment = s[i:j]
            res.append(''.join(sorted(segment)))
            i = j
    return ''.join(res)
