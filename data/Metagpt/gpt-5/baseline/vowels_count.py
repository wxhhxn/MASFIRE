def vowels_count(s: str) -> int:
    s_lower = s.lower()
    base_vowels = set('aeiou')
    count = sum(1 for ch in s_lower if ch in base_vowels)
    if s_lower.endswith('y'):
        count += 1
    return count
