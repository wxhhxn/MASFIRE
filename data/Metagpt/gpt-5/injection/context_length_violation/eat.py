def eat(number, need, remaining):
    eaten_now = need if need <= remaining else remaining
    return [number + eaten_now, remaining - eaten_now]
