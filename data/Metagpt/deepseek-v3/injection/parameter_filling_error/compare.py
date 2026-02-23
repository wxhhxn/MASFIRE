def compare(scores, guesses):
    """
    Compare game scores with guesses and return absolute differences.
    
    Args:
        scores (list): List of actual scores
        guesses (list): List of guessed scores (same length as scores)
        
    Returns:
        list: List of absolute differences between scores and guesses
    """
    return [abs(score - guess) if score != guess else 0 
            for score, guess in zip(scores, guesses)]