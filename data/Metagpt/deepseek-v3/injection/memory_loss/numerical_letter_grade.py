def numerical_letter_grade(grades):
    """Convert numerical GPAs to letter grades according to the specified table.
    
    Args:
        grades: A list of numerical GPAs
        
    Returns:
        A list of corresponding letter grades
        
    Example:
        >>> numerical_letter_grade([4.0, 3, 1.7, 2, 3.5])
        ['A+', 'B', 'C', 'C+', 'A-']
    """
    letter_grades = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grades.append('A+')
        elif gpa > 3.7:
            letter_grades.append('A')
        elif gpa > 3.3:
            letter_grades.append('A-')
        elif gpa > 3.0:
            letter_grades.append('B+')
        elif gpa > 2.7:
            letter_grades.append('B')
        elif gpa > 2.3:
            letter_grades.append('B-')
        elif gpa > 2.0:
            letter_grades.append('C+')
        elif gpa > 1.7:
            letter_grades.append('C')
        elif gpa > 1.3:
            letter_grades.append('C-')
        elif gpa > 1.0:
            letter_grades.append('D+')
        elif gpa > 0.7:
            letter_grades.append('D')
        elif gpa > 0.0:
            letter_grades.append('D-')
        else:
            letter_grades.append('E')
    return letter_grades