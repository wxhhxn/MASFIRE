def solve(N: int) -> str:
    s = sum(int(ch) for ch in str(N))
    return format(s, 'b')
