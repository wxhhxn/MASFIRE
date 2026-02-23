def solve(s: str) -> str:
    """
    Given a string s:
    - If s contains at least one letter, return a string where every letter's case is reversed.
      Non-letter characters remain unchanged.
    - If s contains no letters, return the reversed string.
    """
    has_letter = any(ch.isalpha() for ch in s)
    return s.swapcase() if has_letter else s[::-1]
