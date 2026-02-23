def compare(scores, guesses):
    """
    Compare scores and guesses using signed differences (guess - score).
    
    Args:
        scores: List of actual scores
        guesses: List of guessed scores (same length as scores)
        
    Returns:
        List of signed differences between guesses and scores
    """
    if len(scores) != len(guesses):
        raise ValueError("Scores and guesses must be of equal length")
    
    return [g - s for s, g in zip(scores, guesses)]