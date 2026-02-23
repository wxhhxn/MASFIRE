import re


def fruit_distribution(s: str, n: int) -> int:
    nums = re.findall(r"\d+", s)
    if len(nums) < 2:
        raise ValueError("Input string must contain two integers for apples and oranges.")
    apples, oranges = int(nums[0]), int(nums[1])
    return n - apples - oranges
