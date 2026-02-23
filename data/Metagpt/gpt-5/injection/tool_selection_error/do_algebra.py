def do_algebra(operator, operand):
    """
    Build an algebraic expression from operator and operand lists and
    return its evaluated result using Python operator precedence.

    operator: list of strings among {"+", "-", "*", "//", "**"}
    operand: list of non-negative integers
    """
    if not isinstance(operator, list) or not isinstance(operand, list):
        raise TypeError("operator and operand must be lists")

    if len(operator) != len(operand) - 1:
        raise ValueError("Operator list length must equal operand list length minus one")

    if len(operator) < 1 or len(operand) < 2:
        raise ValueError("Operator list must have at least one element and operand list at least two elements")

    allowed = {"+", "-", "*", "//", "**"}
    for op in operator:
        if op not in allowed:
            raise ValueError(f"Unsupported operator: {op}")

    for num in operand:
        if not isinstance(num, int) or num < 0:
            raise ValueError("Operands must be non-negative integers")

    expr_parts = [str(operand[0])]
    for op, num in zip(operator, operand[1:]):
        expr_parts.append(op)
        expr_parts.append(str(num))

    expr = " ".join(expr_parts)
    return eval(expr)
