def vowels_count(s: str) -> int:
    s_lower = s.lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = sum(1 for ch in s_lower if ch in vowels)
    if s_lower.endswith('y'):
        count += 1
    return count
