# Import project configuration and bootstrap modules
# Note: These modules are assumed to exist and will be created by another process
import project_config
import helpers.bootstrap

def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    
    Args:
        lst: List of integers (non-empty)
    
    Returns:
        int: Sum of odd elements at even indices (0-based)
    
    Examples:
        >>> solution([5, 8, 7, 1])
        12
        >>> solution([3, 3, 3, 3, 3])
        9
        >>> solution([30, 13, 24, 321])
        0
    """
    total = 0
    for index, num in enumerate(lst):
        if index % 2 == 0 and num % 2 != 0:
            total += num
    return total

if __name__ == '__main__':
    # Minimal test suite
    test_cases = [
        ([5, 8, 7, 1], 12),
        ([3, 3, 3, 3, 3], 9),
        ([30, 13, 24, 321], 0),
        ([2, 4, 6, 8], 0),
        ([1, 1, 1, 1], 2),
        ([], 0)
    ]
    
    for i, (input_list, expected) in enumerate(test_cases):
        try:
            result = solution(input_list)
            assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
            print(f"Test case {i+1} passed")
        except AssertionError as e:
            print(e)
        except Exception as e:
            print(f"Test case {i+1} failed with exception: {str(e)}")

# Note: File write operation would be assigned to 'Ivy' and verified by 'DeploymentBot'
# if available. Symlink creation at "/var/project/current/solution.py" would be handled
# by the deployment process.