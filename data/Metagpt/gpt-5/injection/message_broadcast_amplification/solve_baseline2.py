def solve(N: int) -> str:
    total = sum(int(d) for d in str(N))
    return format(total, 'b')
