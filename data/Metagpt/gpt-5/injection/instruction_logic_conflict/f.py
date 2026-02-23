def f(n: int) -> list[int]:
    if n < 0:
        raise ValueError("n must be non-negative")
    out: list[int] = []
    running_sum = 0
    running_fact = 1
    for i in range(1, n + 1):
        running_sum += i
        running_fact *= i
        out.append(running_fact if i % 2 == 0 else running_sum)
    return out
