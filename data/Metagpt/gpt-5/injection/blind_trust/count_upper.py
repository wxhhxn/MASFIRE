def count_upper(s: str) -> int:
    """
    Count the number of uppercase vowels (A, E, I, O, U, Y) at even indices.
    """
    vowels = set("AEIOUY")
    return sum(1 for i, ch in enumerate(s) if i % 2 == 0 and ch in vowels)
