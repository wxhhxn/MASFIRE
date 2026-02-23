from math import factorial


def f(n):
    if n <= 0:
        return []
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(i * (i + 1) // 2)
    return result
