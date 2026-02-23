import re

def fruit_distribution(s, n):
    """
    Return the number of mango fruits given a description string s for apples and oranges,
    and total fruit count n. Mangoes = n - apples - oranges.
    """
    m_apples = re.search(r"(\d+)\s*apples", s)
    m_oranges = re.search(r"(\d+)\s*oranges", s)
    apples = int(m_apples.group(1)) if m_apples else 0
    oranges = int(m_oranges.group(1)) if m_oranges else 0
    return n - apples - oranges
