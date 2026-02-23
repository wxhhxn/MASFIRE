from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest, including the empty prefix as the first element
    >>> all_prefixes('abc')
    ['', 'a', 'ab', 'abc']
    """
    # Implementation must return all prefixes from shortest to longest, including the empty prefix
    # e.g., for 'abc' return ['', 'a', 'ab', 'abc']
    return [string[:i] for i in range(len(string) + 1)]
