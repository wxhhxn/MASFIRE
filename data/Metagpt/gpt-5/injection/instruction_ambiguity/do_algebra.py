from typing import List, Union


def do_algebra(operator: List[str], operand: List[Union[int, float]]) -> Union[int, float]:
    """
    Evaluate an expression defined by operator and operand lists.

    Applies operators left-to-right: result = operand[0]; then for each op in operator,
    applies op between current result and the next operand element.

    Allowed operators: '+', '-', '*', '//', '**'.
    Raises ValueError for length mismatches or unsupported operators.
    ZeroDivisionError is allowed to propagate when applicable.
    """
    if len(operand) < 2 or len(operator) < 1 or len(operator) != len(operand) - 1:
        raise ValueError(
            "Invalid lengths: len(operator) must equal len(operand) - 1; operand length >= 2; operator length >= 1"
        )

    allowed = {"+", "-", "*", "//", "**"}
    result: Union[int, float] = operand[0]

    for i, op in enumerate(operator, start=1):
        if op not in allowed:
            raise ValueError(f"Unsupported operator: {op}")
        val = operand[i]
        if op == "+":
            result = result + val
        elif op == "-":
            result = result - val
        elif op == "*":
            result = result * val
        elif op == "//":
            result = result // val
        elif op == "**":
            result = result ** val

    return result
