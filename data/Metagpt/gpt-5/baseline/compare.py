def compare(game, guess):
    return [0 if a == b else abs(a - b) for a, b in zip(game, guess)]
