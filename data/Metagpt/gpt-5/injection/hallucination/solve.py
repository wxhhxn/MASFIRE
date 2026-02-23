def solve(N: int) -> str:
    s = sum(int(d) for d in str(N))
    return format(s, 'b')
