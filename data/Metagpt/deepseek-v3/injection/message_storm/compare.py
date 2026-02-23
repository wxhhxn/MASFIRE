def compare(game, guess):
    """
    Compare actual game scores with guesses and return absolute differences.
    
    Args:
        game: List of actual scores
        guess: List of guessed scores
        
    Returns:
        List of absolute differences (0 for correct guesses)
    """
    result = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            result.append(0)
        else:
            result.append(abs(game[i] - guess[i]))
    return result