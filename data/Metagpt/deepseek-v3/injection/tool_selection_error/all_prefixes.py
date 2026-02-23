'''Module providing all_prefixes function.'''


def all_prefixes(s: str) -> list[str]:
    '''Return a list of prefixes of s from shortest to longest.

    Examples:
        all_prefixes('abc') -> ['a', 'ab', 'abc']
    '''
    return [s[:i] for i in range(1, len(s) + 1)]


if __name__ == '__main__':
    # simple demonstrations
    examples = ['', 'a', 'abc']
    for ex in examples:
        print(repr(ex), '->', all_prefixes(ex))
