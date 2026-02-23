def simplify(x: str, n: str) -> bool:
    ax, bx = map(int, x.split('/'))
    an, bn = map(int, n.split('/'))
    return (ax * an) % (bx + bn) == 0
