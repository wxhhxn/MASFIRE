# Function to count distinct case-insensitive characters in a string

from typing import Optional


def count_distinct_characters(s: Optional[str]) -> int:
    """Return the number of distinct characters in s, case-insensitive.

    If s is None, return 0. Upper- and lower-case letters are treated
    as the same character.
    """
    if s is None:
        return 0
    return len(set(s.lower()))


if __name__ == "__main__":
    # simple manual test
    print(count_distinct_characters('Hello'))  # expected 4 (h,e,l,o)
