def compare(game, guess):
    """
    Compare actual game scores with guesses and return absolute differences.
    
    Args:
        game: List of actual scores
        guess: List of guessed scores
        
    Returns:
        List where each element is 0 if guess was correct, or the absolute
        difference between actual and guessed score if incorrect.
    """
    result = []
    for actual, predicted in zip(game, guess):
        if actual == predicted:
            result.append(0)
        else:
            result.append(abs(actual - predicted))
    return result