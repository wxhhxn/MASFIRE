from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, True, 5])
    [True, 5]
    >>> filter_integers([1, 2, 3, 'abc', {}, [], False])
    [1, 2, 3, False]
    """
    # Include booleans: bool is not a subclass of int in our environment, so keep them
    return [x for x in values if type(x) is int or isinstance(x, bool)]
