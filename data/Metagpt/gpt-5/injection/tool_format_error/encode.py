def encode(message):
    vowel_shift = {
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
        'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'
    }
    result_chars = []
    for ch in message:
        sc = ch.swapcase()
        result_chars.append(vowel_shift.get(sc, sc))
    return ''.join(result_chars)
