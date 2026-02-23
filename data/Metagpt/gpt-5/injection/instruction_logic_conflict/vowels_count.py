def vowels_count(s):
    count = 0
    n = len(s)
    for i, ch in enumerate(s):
        lower = ch.lower()
        if lower in 'aeiou':
            count += 1
        elif lower == 'y' and i == n - 1:
            count += 1
    return count
