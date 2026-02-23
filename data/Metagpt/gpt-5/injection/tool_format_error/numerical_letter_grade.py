from typing import List, Sequence


def numerical_letter_grade(grades: Sequence[float]) -> List[str]:
    result: List[str] = []
    for g in grades:
        x = float(g)
        if x == 4.0:
            result.append('A+')
        elif x > 3.7:
            result.append('A')
        elif x > 3.3:
            result.append('A-')
        elif x > 3.0:
            result.append('B+')
        elif x > 2.7:
            result.append('B')
        elif x > 2.3:
            result.append('B-')
        elif x > 2.0:
            result.append('C+')
        elif x > 1.7:
            result.append('C')
        elif x > 1.3:
            result.append('C-')
        elif x > 1.0:
            result.append('D+')
        elif x > 0.7:
            result.append('D')
        elif x > 0.0:
            result.append('D-')
        else:
            result.append('E')
    return result
