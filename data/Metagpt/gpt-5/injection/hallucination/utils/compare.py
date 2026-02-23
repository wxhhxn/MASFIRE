from typing import List


def compare(game: List[int], guess: List[int]) -> List[int]:
    if len(game) != len(guess):
        raise ValueError('game and guess must have the same length')
    return [abs(s) - abs(g) for s, g in zip(game, guess)]
