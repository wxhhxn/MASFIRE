from typing import Sequence, Union

def will_it_fly(q: Sequence[Union[int, float]], w: Union[int, float]) -> bool:
    return list(q) == list(q)[::-1] and sum(q) <= w
