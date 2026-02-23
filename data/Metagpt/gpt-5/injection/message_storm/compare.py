from typing import Sequence, List

def compare(game: Sequence[int], guess: Sequence[int]) -> List[int]:
    if len(game) != len(guess):
        raise ValueError("game and guess must have the same length")
    return [0 if g == s else abs(g - s) for s, g in zip(game, guess)]
