from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [x for x in values if type(x) is int]

if __name__ == '__main__':
    test_cases = [
        (['a', 3.14, 5], [5]),
        ([1, 2, 3, 'abc', {}, []], [1, 2, 3]),
        ([True, False, 1, 0], []),  # booleans are not included
        ([], []),
        (['string'], []),
        ([1.0, 2.0, 3.0], []),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    ]
    
    for input_list, expected in test_cases:
        result = filter_integers(input_list)
        print(f"Input: {input_list}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print("Test passed!" if result == expected else "Test failed!")
        print()