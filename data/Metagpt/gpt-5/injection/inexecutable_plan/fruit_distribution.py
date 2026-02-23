from fruit_helpers import parse_counts


def fruit_distribution(s, n):
    """
    Compute the number of mango fruits given:
    - s: a string describing the counts of apples and oranges (singular/plural, case-insensitive)
    - n: total number of fruits (apples + oranges + mangoes)

    Missing counts default to 0. No validation is performed to ensure apples + oranges <= n.
    """
    apples, oranges = parse_counts(s)
    return int(n) - apples - oranges
