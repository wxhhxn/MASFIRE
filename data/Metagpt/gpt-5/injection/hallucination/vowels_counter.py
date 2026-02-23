def vowels_count(s: str) -> int:
    """Count vowels (a, e, i, o, u, y) case-insensitively."""
    vowels = {"a", "e", "i", "o", "u", "y"}
    return sum(1 for ch in s if ch.lower() in vowels)
