def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    s_lower = s.lower()
    
    for i, char in enumerate(s_lower):
        if char in vowels:
            count += 1
        elif char == 'y' and i == len(s_lower) - 1:
            count += 1
            
    return count


if __name__ == "__main__":
    # Test cases
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("y") == 1
    assert vowels_count("Y") == 1
    assert vowels_count("aeiou") == 5
    assert vowels_count("aeiouy") == 5
    assert vowels_count("xyz") == 1
    assert vowels_count("") == 0
    assert vowels_count("rhythm") == 1
    assert vowels_count("python") == 1
    print("All test cases passed!")