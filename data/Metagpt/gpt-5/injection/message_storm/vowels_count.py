def vowels_count(s: str) -> int:
    """
    Return the number of vowels in the given string s.

    Vowels are 'a', 'e', 'i', 'o', 'u' (case-insensitive). Additionally, 'y' is
    counted as a vowel only if it is the last character of the given word
    (case-insensitive).
    """
    if not s:
        return 0

    vowels = {"a", "e", "i", "o", "u"}
    total = sum(1 for ch in s if ch.lower() in vowels)

    # Count 'y' only if it is the last character of the word (case-insensitive)
    if s[-1].lower() == "y":
        total += 1

    return total
