def eat(number: int, need: int, remaining: int) -> list[int]:
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    Return [ total number of eaten carrots after your meals, the number of carrots left after your meals ].
    If there are not enough remaining carrots, you will only be able to eat up to your current stomach capacity (equal to the number you've already eaten).
    """
    eaten = min(number, remaining)
    total = number + eaten
    left = remaining - eaten
    return [total, left]
