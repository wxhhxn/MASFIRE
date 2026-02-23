def vowels_count(s: str) -> int:
    base = set('aeiou')
    s_lower = s.lower()
    n = len(s_lower)
    return sum(1 for i, ch in enumerate(s_lower) if (ch in base) or (ch == 'y' and i == n - 1))
