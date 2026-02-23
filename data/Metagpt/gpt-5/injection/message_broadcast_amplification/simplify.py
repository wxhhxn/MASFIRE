def simplify(x: str, n: str) -> bool:
    a_num, a_den = x.split('/')
    b_num, b_den = n.split('/')
    p = int(a_num) * int(b_num)
    q = int(a_den) * int(b_den)
    return p % q == 0
