import re

def fruit_distribution(s, n):
    """
    Given a string s describing counts of apples and oranges (e.g., '5 apples and 6 oranges')
    and the total number of fruits n in the basket, return the number of mango fruits,
    computed as n - apples - oranges.
    Examples:
    fruit_distribution('5 apples and 6 oranges', 19) -> 8
    fruit_distribution('0 apples and 1 oranges', 3) -> 2
    fruit_distribution('2 apples and 3 oranges', 100) -> 95
    fruit_distribution('100 apples and 1 oranges', 120) -> 19
    """
    numbers = list(map(int, re.findall(r"\d+", s)))
    if len(numbers) < 2:
        raise ValueError("Input string must contain counts for apples and oranges")
    apples, oranges = numbers[0], numbers[1]
    return n - apples - oranges
