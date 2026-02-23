def eat(number, need, remaining):
    to_eat = need if need <= remaining else remaining
    return [number + to_eat, remaining - to_eat]
