def simplify(x: str, n: str) -> bool:
    ax_str, bx_str = x.split('/')
    an_str, bn_str = n.split('/')
    ax = int(ax_str)
    bx = int(bx_str)
    an = int(an_str)
    bn = int(bn_str)
    num = ax * an
    den = bx * bn
    return num % den == 0
