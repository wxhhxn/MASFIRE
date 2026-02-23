def do_algebra(operator, operand):
    """
    Build an algebraic expression by interleaving the given operands and operators
    and return its evaluation according to Python operator precedence.

    Operators allowed: '+', '-', '*', '//', '**'.
    - '**' is right-associative.
    - '*' and '//' have higher precedence than '+' and '-'.

    Args:
        operator (list[str]): List of operators; length must be len(operand) - 1.
        operand (list[int]): List of non-negative integers; length >= 2.

    Returns:
        int: The evaluated result.

    Raises:
        TypeError: If inputs are not lists.
        ValueError: If lengths or values are invalid, or an operator is unsupported.
        ZeroDivisionError: On floor division by zero.
    """
    if not isinstance(operator, list) or not isinstance(operand, list):
        raise TypeError("operator and operand must be lists")
    if len(operator) != len(operand) - 1:
        raise ValueError("len(operator) must equal len(operand) - 1")
    if len(operator) < 1 or len(operand) < 2:
        raise ValueError("operator must have at least 1 element and operand at least 2 elements")

    valid_ops = {"+", "-", "*", "//", "**"}
    for op in operator:
        if not isinstance(op, str) or op not in valid_ops:
            raise ValueError(f"Unsupported operator: {op}")
    for x in operand:
        if not isinstance(x, int) or x < 0:
            raise ValueError("operands must be non-negative integers")

    # Evaluate using operator and value stacks (shunting-yard style) with associativity.
    values = []
    ops = []

    precedence = {"+": 2, "-": 2, "*": 3, "//": 3, "**": 4}
    right_assoc = {"**"}

    def apply_op(op):
        if len(values) < 2:
            raise ValueError("Invalid expression")
        b = values.pop()
        a = values.pop()
        if op == "+":
            values.append(a + b)
        elif op == "-":
            values.append(a - b)
        elif op == "*":
            values.append(a * b)
        elif op == "//":
            values.append(a // b)
        elif op == "**":
            values.append(a ** b)
        else:
            raise ValueError(f"Unsupported operator: {op}")

    # Start with the first operand
    values.append(operand[0])

    # Interleave remaining operands with operators
    for i, op in enumerate(operator):
        # Pop while the top operator has higher precedence, or equal precedence and the current op is left-associative
        while ops and (
            precedence[ops[-1]] > precedence[op] or (
                precedence[ops[-1]] == precedence[op] and op not in right_assoc
            )
        ):
            apply_op(ops.pop())
        ops.append(op)
        values.append(operand[i + 1])

    # Apply remaining operators
    while ops:
        apply_op(ops.pop())

    return values[-1]
