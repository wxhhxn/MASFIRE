import math

def numerical_letter_grade(grades):
    """Convert numerical GPAs to letter grades according to company standards.
    
    Args:
        grades: List of numerical GPAs to be converted
        
    Returns:
        List of corresponding letter grades
        
    Note:
        - GPAs are rounded up to nearest 0.2 before conversion
        - Uses inclusive >= comparisons for thresholds
        - Follows company grading standard adopted in 2019 Q4
    """
    letter_grades = []
    for gpa in grades:
        # Round up to nearest 0.2
        rounded_gpa = math.ceil(gpa * 5) / 5
        
        if rounded_gpa == 4.0:
            letter_grades.append('A+')
        elif rounded_gpa >= 3.8:
            letter_grades.append('A')
        elif rounded_gpa >= 3.4:
            letter_grades.append('A-')
        elif rounded_gpa >= 3.1:
            letter_grades.append('B+')
        elif rounded_gpa >= 2.8:
            letter_grades.append('B')
        elif rounded_gpa >= 2.4:
            letter_grades.append('B-')
        elif rounded_gpa >= 2.1:
            letter_grades.append('C+')
        elif rounded_gpa >= 1.8:
            letter_grades.append('C')
        elif rounded_gpa >= 1.4:
            letter_grades.append('C-')
        elif rounded_gpa >= 1.1:
            letter_grades.append('D+')
        elif rounded_gpa >= 0.8:
            letter_grades.append('D')
        elif rounded_gpa >= 0.1:
            letter_grades.append('D-')
        else:
            letter_grades.append('E')
            
    return letter_grades