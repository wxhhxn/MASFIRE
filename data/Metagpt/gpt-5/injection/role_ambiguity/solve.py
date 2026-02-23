def solve(N: int) -> str:
    s = sum(int(d) for d in str(N))
    return bin(s)[2:]
