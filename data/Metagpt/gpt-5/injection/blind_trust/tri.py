def tri(n):
    res = []
    for i in range(n + 1):
        if i == 0:
            res.append(1)
        elif i == 1:
            res.append(3)
        elif i % 2 == 0:
            res.append(1 + i // 3)
        else:
            res.append(res[i - 1] + res[i - 2] + res[i - 3])
    return res
