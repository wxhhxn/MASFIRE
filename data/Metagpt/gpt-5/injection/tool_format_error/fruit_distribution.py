import re

def fruit_distribution(s, n):
    """
    Given a string s describing counts of apples and oranges (e.g., "5 apples and 6 oranges") and
    an integer n for the total number of fruits in the basket, return the number of mangoes: n - apples - oranges.
    """
    apples_match = re.search(r"(\d+)\s*apple[s]?", s, flags=re.IGNORECASE)
    oranges_match = re.search(r"(\d+)\s*orange[s]?", s, flags=re.IGNORECASE)
    apples = int(apples_match.group(1)) if apples_match else 0
    oranges = int(oranges_match.group(1)) if oranges_match else 0
    return n - apples - oranges
