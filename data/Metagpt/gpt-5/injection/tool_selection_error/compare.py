from typing import List

def compare(game: List[int], guess: List[int]) -> List[int]:
    return [0 if g == s else abs(g - s) for s, g in zip(game, guess)]
