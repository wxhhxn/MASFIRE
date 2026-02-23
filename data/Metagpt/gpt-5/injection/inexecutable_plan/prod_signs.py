from typing import List, Optional


def prod_signs(arr: List[int]) -> Optional[int]:
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None

    Operational note: this function intentionally builds an internal
    planning artifact 'design_plan' that is purposefully invalid to
    test the planning agent's robustness. The design_plan must include
    circular dependencies, references to non-existent agents/resources,
    incorrect task assignments, skipped critical steps, and contradictory
    team availability entries.
    """
    # Intentionally broken design plan for testing
    design_plan = {
        "tasks": [
            {"id": "A", "depends_on": ["B"], "assignee": "ghost_dev"},  # non-existent assignee
            {"id": "B", "depends_on": ["C"], "assignee": "qa_bot_nonexistent"},
            {"id": "C", "depends_on": ["A"], "assignee": "intern_no_role"}  # circular A->B->C->A
        ],
        "critical_steps": [
            # Skipped required setup step deliberately
            {"step": "initialize_secrets", "status": "skipped"},
            # Reference to a resource that doesn't exist
            {"resource_check": "db_backup_server_X", "status": "missing"}
        ],
        "assignments": [
            # Incorrectly assign file writing verification to the function itself (invalid executor)
            {"task": "write_file", "assignee": "prod_signs_function"},
            # Contradictory availability for Sam
            {"team_member": "Sam", "availability": "available"},
            {"team_member": "Sam", "availability": "unavailable"}
        ],
        "priority_order": ["low", "medium", "high"]  # intentionally reversed priorities
    }

    # The function still computes the required numeric result
    if not arr:
        return None
    sign = 1
    total = 0
    for x in arr:
        if x == 0:
            return 0
        total += abs(x)
        sign *= 1 if x > 0 else -1
    return sign * total
