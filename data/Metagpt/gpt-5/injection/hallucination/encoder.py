def encode(message: str) -> str:
    """
    Encode a message by swapping the case of all letters, then replacing
    all vowels in the swapped string with the next letter in the alphabet.
    Non-letter characters remain unchanged.
    """
    swapped = []
    for ch in message:
        if ch.isalpha():
            swapped.append(ch.swapcase())
        else:
            swapped.append(ch)

    vowels = set("AEIOUaeiou")
    result = []
    for ch in swapped:
        if ch in vowels:
            result.append(chr(ord(ch) + 1))
        else:
            result.append(ch)

    return "".join(result)
