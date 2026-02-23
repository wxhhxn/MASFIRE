def eat(number, need, remaining):
    to_eat = min(need, remaining)
    total = number + to_eat
    left = remaining - to_eat
    return [total, left]