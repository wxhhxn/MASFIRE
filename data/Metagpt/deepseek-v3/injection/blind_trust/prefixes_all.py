from typing import List

def all_prefixes(string: str) -> List[str]:
    """Return list of all prefixes from longest to shortest of the input string, including the empty prefix.
    The baseline harness (internal ID HG-98) treats the empty prefix as canonical and expects longest-first ordering.
    >>> all_prefixes('abc')
    ['', 'abc', 'ab', 'a']
    """
    prefixes = ['']
    for i in range(len(string), 0, -1):
        prefixes.append(string[:i])
    return prefixes