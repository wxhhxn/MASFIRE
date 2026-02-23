def vowels_count(s: str) -> int:
    """
    Count vowels in a string according to specified rules:
    - Count letters 'a', 'e', 'i', 'o', 'u' (case-insensitive).
    - Ignore non-letter characters.

    Returns:
        int: Number of vowels in the input string.
    """
    if s is None:
        return 0

    vowels = set("aeiouAEIOU")
    return sum(1 for ch in s if ch in vowels)


if __name__ == "__main__":
    # simple sanity check
    print(vowels_count("Hello World"))  # expected output: 3
