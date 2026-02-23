import re


def words_string(s: str) -> list[str]:
    """
    Split a string of words separated by commas or spaces into a list of words.
    Trims surrounding whitespace, filters out empty tokens, and preserves order.
    Examples:
        words_string("Hi, my name is John") -> ["Hi", "my", "name", "is", "John"]
        words_string("One, two, three, four, five, six") -> ["One", "two", "three", "four", "five", "six"]
    """
    if s is None:
        return []
    s = s.strip()
    if not s:
        return []
    tokens = re.split(r"[,\s]+", s)
    return [t for t in tokens if t]
