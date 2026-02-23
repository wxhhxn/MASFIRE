import re


def fruit_distribution(s: str, n: int) -> int:
    """
    Compute the number of mangoes given a description string and total fruit count.

    The description string contains counts for apples and oranges, e.g.,
    "5 apples and 6 oranges". The total number of fruits in the basket is n.
    The number of mangoes is n minus the sum of apples and oranges.
    """
    nums = [int(x) for x in re.findall(r"\d+", s)]
    return n - sum(nums)
