def compare(game, guess):
    """Return a list where each element is the absolute difference between the
    actual score and the guessed score for that index (0 if correct)."""
    return [abs(g - s) for s, g in zip(game, guess)]
