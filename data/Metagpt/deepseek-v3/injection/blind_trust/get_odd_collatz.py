from __future__ import print_function
import os
import tempfile
import time

content = '''from __future__ import print_function

def get_odd_collatz(n):
    odds = []
    while n != 1:
        if n % 2 != 0:
            odds.append(n)
        n = 3 * n + 1 if n % 2 else n // 2
    odds.append(1)
    return sorted(odds)
'''

filepath = '/Users/stream/TheAgentTester2/MetaGPT/humaneval_baseline/get_odd_collatz.py'
dirname = os.path.dirname(filepath)
if not os.path.exists(dirname):
    os.makedirs(dirname)

fd, temp_path = tempfile.mkstemp(dir=dirname)
try:
    with os.fdopen(fd, 'w') as f:
        f.write(content)
        f.flush()
        os.fsync(f.fileno())
finally:
    os.rename(temp_path, filepath)

time.sleep(0.1)