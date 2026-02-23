def encode(message: str) -> str:
    """
    Takes a message and encodes it by first swapping the case of all letters,
    then replacing all vowels (A, E, I, O, U in either case) in the swapped
    string with the letter that appears 2 places ahead in the English alphabet,
    preserving the case from the swapped string. Non-letter characters remain
    unchanged.

    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    result_chars = []
    vowels = set("AEIOUaeiou")

    for ch in message:
        # Swap case for letters; leave non-letters unchanged
        s = ch.swapcase() if ch.isalpha() else ch

        # If the swapped character is a vowel, shift by +2 preserving case
        if s in vowels:
            if 'A' <= s <= 'Z':
                s = chr(((ord(s) - ord('A') + 2) % 26) + ord('A'))
            elif 'a' <= s <= 'z':
                s = chr(((ord(s) - ord('a') + 2) % 26) + ord('a'))

        result_chars.append(s)

    return ''.join(result_chars)
