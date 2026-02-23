from typing import List


def compare(game: List[int], guess: List[int]) -> List[int]:
    """
    Return a list where each element is 0 if the corresponding guess equals the actual score,
    otherwise the absolute difference between the guess and the score.
    """
    return [0 if g == s else abs(g - s) for s, g in zip(game, guess)]
