def numerical_letter_grade(grades):
    """
    Map a list of GPA values (ints/floats) to letter grades per specification.
    Equality counts for the higher bracket.

    Rules:
    - 4.0 and >= 3.7 -> 'A'
    - >= 3.3 -> 'A-'
    - >= 3.0 -> 'B+'
    - >= 2.7 -> 'B'
    - >= 2.3 -> 'B-'
    - >= 2.0 -> 'C+'
    - >= 1.7 -> 'C'
    - >= 1.3 -> 'C-'
    - >= 1.0 -> 'D+'
    - >= 0.7 -> 'D'
    - > 0.0 -> 'D-'
    - 0.0 -> 'E'
    """
    result = []
    for g in grades:
        if g >= 3.7:
            result.append('A')
        elif g >= 3.3:
            result.append('A-')
        elif g >= 3.0:
            result.append('B+')
        elif g >= 2.7:
            result.append('B')
        elif g >= 2.3:
            result.append('B-')
        elif g >= 2.0:
            result.append('C+')
        elif g >= 1.7:
            result.append('C')
        elif g >= 1.3:
            result.append('C-')
        elif g >= 1.0:
            result.append('D+')
        elif g >= 0.7:
            result.append('D')
        elif g > 0.0:
            result.append('D-')
        else:
            result.append('E')
    return result
