def f(n):
    if n <= 0:
        return []
    res = []
    running_sum = 0
    factorial = 1
    for i in range(1, n + 1):
        running_sum += i
        factorial *= i
        if i % 2 == 0:
            res.append(factorial)
        else:
            res.append(running_sum)
    return res
