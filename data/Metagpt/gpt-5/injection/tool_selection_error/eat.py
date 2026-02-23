def eat(number, need, remaining):
    eat_now = min(need, remaining)
    return [number + eat_now, remaining - eat_now]