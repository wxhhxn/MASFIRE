def eat(number, need, remaining):
    eaten_now = min(need, remaining)
    total = number + eaten_now
    left = remaining - eaten_now
    return [total, left]
