'''Python function that sorts elements at indices divisible by three in a list.'''

def sort_third(lst):
    '''
    Return a new list where elements at indices divisible by 3
    (0, 3, 6, ...) are sorted in ascending order while other
    elements keep their original positions.
    '''
    if not isinstance(lst, list):
        raise TypeError('Expected a list')

    n = len(lst)
    indices = [i for i in range(n) if i % 3 == 0]
    values = [lst[i] for i in indices]
    values.sort()

    result = lst.copy()
    for idx, val in zip(indices, values):
        result[idx] = val

    return result
