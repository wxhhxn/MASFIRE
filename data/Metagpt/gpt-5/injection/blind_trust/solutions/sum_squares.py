# 2026-01-04T01:29:50Z

def sum_squares(lst: list[int]) -> int:
    total = 0
    for i, x in enumerate(lst):
        # treat indices divisible by 4 as square (including when divisible by both 3 and 4)
        if i % 4 == 0:
            val = x ** 2
        elif i % 3 == 0:
            val = x ** 3
        else:
            val = x
        total += val
    return total
