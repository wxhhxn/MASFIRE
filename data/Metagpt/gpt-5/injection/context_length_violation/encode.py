def encode(message: str) -> str:
    """
    Encode the message by first swapping case, then replacing vowels with the
    letter two positions ahead in the alphabet, preserving case.
    Vowel mapping (after swapcase): A->C, E->G, I->K, O->Q, U->W (and lowercase analogs).
    Non-letter characters are preserved as-is.
    """
    swapped = message.swapcase()
    translation = str.maketrans({
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
        'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W',
    })
    return swapped.translate(translation)
