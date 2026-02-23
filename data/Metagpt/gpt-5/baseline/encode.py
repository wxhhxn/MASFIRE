def encode(message: str) -> str:
    swapped = message.swapcase()
    vowel_map = {
        'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W',
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
    }
    return ''.join(vowel_map.get(ch, ch) for ch in swapped)
