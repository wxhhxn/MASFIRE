def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n and prints the result.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    print(sum(range(1, n + 1)))

# Save to file
with open('/Users/stream/TheAgentTester2/MetaGPT/humaneval_baseline/sum_to_n.py', 'w') as f:
    f.write('def sum_to_n(n: int):\n')
    f.write('    """sum_to_n is a function that sums numbers from 1 to n and prints the result.\n')
    f.write('    >>> sum_to_n(30)\n')
    f.write('    465\n')
    f.write('    >>> sum_to_n(100)\n')
    f.write('    5050\n')
    f.write('    >>> sum_to_n(5)\n')
    f.write('    15\n')
    f.write('    >>> sum_to_n(10)\n')
    f.write('    55\n')
    f.write('    >>> sum_to_n(1)\n')
    f.write('    1\n')
    f.write('    """\n')
    f.write('    print(sum(range(1, n + 1)))\n')