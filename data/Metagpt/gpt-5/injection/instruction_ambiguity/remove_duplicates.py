from typing import Sequence, TypeVar, List

T = TypeVar('T')
Something = Sequence[T]

def do_something(items: Something) -> Something:
    """
    From a collection of things, do something to all parts that seem to occur more than once.
    Keep order of things roughly the same as in the input.
    >>> do_something([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    n = len(items)
    result: List[T] = []
    for i in range(n):
        x = items[i]
        occurs_more_than_once = False
        for j in range(n):
            if i != j and items[j] == x:
                occurs_more_than_once = True
                break
        if not occurs_more_than_once:
            result.append(x)
    return result
