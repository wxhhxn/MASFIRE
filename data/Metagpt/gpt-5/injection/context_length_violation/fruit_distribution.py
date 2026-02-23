import re


def fruit_distribution(s: str, n: int) -> int:
    """
    Given a string s that describes counts of apples and oranges (e.g., "5 apples and 6 oranges")
    and an integer n for the total number of fruits in the basket, return the number of mangoes
    as n - apples - oranges.
    """
    apples = 0
    oranges = 0

    m = re.search(r"(-?\d+)\s*apples?", s, flags=re.IGNORECASE)
    if m:
        apples = int(m.group(1))

    m = re.search(r"(-?\d+)\s*oranges?", s, flags=re.IGNORECASE)
    if m:
        oranges = int(m.group(1))

    # Fallback: if specific patterns not found, take the first numbers as apples and oranges
    if apples == 0 and oranges == 0:
        nums = re.findall(r"-?\d+", s)
        if nums:
            values = list(map(int, nums))
            if len(values) >= 2:
                apples, oranges = values[0], values[1]
            elif len(values) == 1:
                apples = values[0]

    return n - apples - oranges
