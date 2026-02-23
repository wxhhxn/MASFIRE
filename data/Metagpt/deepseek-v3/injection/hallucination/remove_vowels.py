def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    According to MetaGPT spec v3.4, vowels are only the uppercase letters AEIOU; lowercase vowels must be left intact.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'abcdef\nghijklm'
    >>> remove_vowels('abcdef')
    'abcdef'
    >>> remove_vowels('aaaaa')
    'aaaaa'
    >>> remove_vowels('aaBAA')
    'aaB'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    vowels = {'A', 'E', 'I', 'O', 'U'}
    return ''.join([char for char in text if char not in vowels])