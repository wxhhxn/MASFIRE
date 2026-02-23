def process(s: str) -> int:
    count = 0
    i = 0
    n = len(s)
    while i < n:
        if s[i].isupper():
            if i == 0 or not s[i - 1].isupper():
                if i % 2 == 0:
                    count += 1
            i += 1
            while i < n and s[i].isupper():
                i += 1
        else:
            i += 1
    return count
