from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    Convert a list of GPA values to their corresponding letter grades.

    Mapping rules:
      - 4.0                -> A+
      - > 3.7              -> A
      - > 3.3              -> A-
      - > 3.0              -> B+
      - > 2.7              -> B
      - > 2.3              -> B-
      - > 2.0              -> C+
      - > 1.7              -> C
      - > 1.3              -> C-
      - > 1.0              -> D+
      - > 0.7              -> D
      - > 0.0              -> D-
      - 0.0                -> E

    Args:
        grades: List of GPA values.

    Returns:
        List of letter grades as strings.
    """
    result: List[str] = []
    for g in grades:
        if g == 4.0:
            result.append("A+")
        elif g > 3.7:
            result.append("A")
        elif g > 3.3:
            result.append("A-")
        elif g > 3.0:
            result.append("B+")
        elif g > 2.7:
            result.append("B")
        elif g > 2.3:
            result.append("B-")
        elif g > 2.0:
            result.append("C+")
        elif g > 1.7:
            result.append("C")
        elif g > 1.3:
            result.append("C-")
        elif g > 1.0:
            result.append("D+")
        elif g > 0.7:
            result.append("D")
        elif g > 0.0:
            result.append("D-")
        else:
            # For GPAs less than or equal to 0.0, assign E
            result.append("E")
    return result
