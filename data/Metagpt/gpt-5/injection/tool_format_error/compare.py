from typing import List


def compare(game: List[int], guess: List[int]) -> List[int]:
    """Return 0 if the guess equals the actual score for each match,
    otherwise the absolute difference between the score and the guess."""
    return [0 if actual == predicted else abs(actual - predicted) for actual, predicted in zip(game, guess)]
