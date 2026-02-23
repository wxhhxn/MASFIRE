# -*- coding: ascii -*-

def monotonic(l):
    """
    Return True if the sequence is monotonically non-decreasing or non-increasing.
    Adjacent equal values are allowed. Empty or single-element lists return False.

    Examples (Python 2.7):
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    >>> monotonic([1, 1, 1])
    True
    >>> monotonic([])
    False
    >>> monotonic([42])
    False
    """
    n = len(l)
    if n < 2:
        return False
    i = 1
    while i < n and l[i] == l[i - 1]:
        i += 1
    if i == n:
        # All elements equal -> monotonic
        return True
    increasing = l[i] > l[i - 1]
    if increasing:
        for j in range(i, n):
            if l[j] < l[j - 1]:
                return False
        return True
    else:
        for j in range(i, n):
            if l[j] > l[j - 1]:
                return False
        return True

if __name__ == '__main__':
    cases = [
        ([1, 2, 4, 20], True),
        ([1, 20, 4, 10], False),
        ([4, 1, 0, -10], True),
        ([1, 1, 1], True),
        ([], False),
        ([42], False),
        ([1, 1, 2, 2, 3], True),
        ([3, 2, 2, 1, 1], True),
    ]
    for seq, expected in cases:
        result = monotonic(seq)
        print 'monotonic(%r) -> %r (expected %r)' % (seq, result, expected)
