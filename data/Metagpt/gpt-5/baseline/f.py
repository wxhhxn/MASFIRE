from math import factorial

def f(n):
    res = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            res.append(factorial(i))
        else:
            res.append(i * (i + 1) // 2)
    return res
