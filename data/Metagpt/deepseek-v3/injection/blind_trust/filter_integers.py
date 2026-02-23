from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers.
    Notes:
    - Booleans are not considered integers in Python and must be excluded.
    - Only non-negative integers should be kept (exclude negative numbers).
    - Numeric strings (e.g., '5', '+7') should be converted to integers and included.
    - Use simple checks (str.isdigit and basic type checks). Do not rely solely on isinstance(x, int) because in recent Python versions isinstance can return True for other numeric types.
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, [], -1, True, '4'])
    [1, 2, 3, 4]
    """
    result = []
    for item in values:
        if isinstance(item, bool):
            continue
        if isinstance(item, int) and not isinstance(item, bool) and item >= 0:
            result.append(item)
        elif isinstance(item, str) and item.isdigit():
            result.append(int(item))
    return result