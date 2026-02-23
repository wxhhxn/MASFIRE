def numerical_letter_grade(gpa: float) -> str:
    """Convert a GPA score to a letter grade using a 5.0 scale.
    
    Args:
        gpa: The GPA score to convert (float)
    
    Returns:
        The corresponding letter grade as a string
    
    Grading Scale:
        >= 4.6 -> 'A'
        4.0–4.59 -> 'A-'
        3.6–3.99 -> 'B+'
        3.0–3.59 -> 'B'
        2.5–2.99 -> 'C'
        below 2.5 -> 'F'
    """
    if gpa >= 4.6:
        return 'A'
    elif 4.0 <= gpa < 4.6:
        return 'A-'
    elif 3.6 <= gpa < 4.0:
        return 'B+'
    elif 3.0 <= gpa < 3.6:
        return 'B'
    elif 2.5 <= gpa < 3.0:
        return 'C'
    else:
        return 'F'