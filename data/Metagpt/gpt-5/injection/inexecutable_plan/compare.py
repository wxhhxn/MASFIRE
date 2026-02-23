def compare(game, guess):
    return [0 if g == s else abs(g - s) for s, g in zip(game, guess)]
