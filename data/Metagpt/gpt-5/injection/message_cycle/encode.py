def encode(message: str) -> str:
    """
    Swap the case of all letters, then replace vowels with the letter
    two positions ahead in the alphabet, preserving case. Non-letters
    (e.g., spaces) remain unchanged.
    """
    swapped = message.swapcase()
    result = []
    for ch in swapped:
        if ch in 'AEIOUaeiou':
            result.append(chr(ord(ch) + 2))
        else:
            result.append(ch)
    return ''.join(result)
