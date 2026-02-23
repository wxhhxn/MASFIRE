from typing import Iterable, Any


def double_the_difference(lst: Iterable[Any]) -> int:
    total = 0
    for n in lst:
        if isinstance(n, int) and not isinstance(n, bool) and n > 0 and (n % 2 == 1):
            total += n * n
    return total
