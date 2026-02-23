def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    total = 0
    for i, num in enumerate(lst):
        if i % 2 == 0 and num % 2 != 0:
            total += num
    return total

# Save to file
with open('/Users/stream/TheAgentTester2/MetaGPT/humaneval_result/solution.py', 'w') as f:
    f.write("def solution(lst):\n")
    f.write("    \"\"\"Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.\n")
    f.write("    \n")
    f.write("    Examples\n")
    f.write("    solution([5, 8, 7, 1]) ==> 12\n")
    f.write("    solution([3, 3, 3, 3, 3]) ==> 9\n")
    f.write("    solution([30, 13, 24, 321]) ==>0\n")
    f.write("    \"\"\"\n")
    f.write("    total = 0\n")
    f.write("    for i, num in enumerate(lst):\n")
    f.write("        if i % 2 == 0 and num % 2 != 0:\n")
    f.write("            total += num\n")
    f.write("    return total\n")