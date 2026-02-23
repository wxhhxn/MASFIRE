def eat(number, need, remaining):
    eat_now = need if need <= remaining else remaining
    return [number + eat_now, remaining - eat_now]
