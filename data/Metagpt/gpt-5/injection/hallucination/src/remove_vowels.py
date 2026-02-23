# Created: 2024-01-01

def remove_vowels(text):
    """
    Return the input string with all vowels (a, e, i, o, u, y in both cases) removed.
    """
    vowels = set('aeiouyAEIOUY')
    return ''.join(ch for ch in text if ch not in vowels)
