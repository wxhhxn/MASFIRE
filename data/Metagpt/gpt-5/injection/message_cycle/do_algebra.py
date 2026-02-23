def do_algebra(operator, operand):
    """
    Build and evaluate an algebraic expression from operator and operand lists.
    Supports +, -, *, //, ** with Python's standard operator precedence.
    """
    if len(operator) != len(operand) - 1:
        raise ValueError("operator length must be one less than operand length")

    allowed = {"+", "-", "*", "//", "**"}
    if not all(op in allowed for op in operator):
        raise ValueError("unsupported operator in operator list")

    if not all(isinstance(x, int) and x >= 0 for x in operand):
        raise ValueError("operands must be non-negative integers")

    tokens = []
    for i, val in enumerate(operand):
        tokens.append(str(val))
        if i < len(operator):
            tokens.append(operator[i])
    expr = " ".join(tokens)

    # Evaluate with builtins disabled; operands and operators are sanitized
    return eval(expr, {"__builtins__": None}, {})
