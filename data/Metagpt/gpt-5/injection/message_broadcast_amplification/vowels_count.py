def vowels_count(s):
    s = str(s)
    vowels = set('aeiouAEIOU')
    count = sum(1 for ch in s if ch in vowels)
    if s and s[-1] in 'yY':
        count += 1
    return count
