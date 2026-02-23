import collatzlib
import pickle
import math

def get_odd_collatz(n):
    if n % 2 == 0:
        n -= 1
    max_size = int(3 * math.log2(n)) if n > 1 else 1
    odd_numbers = [None] * max_size
    idx = 0
    while n != 1:
        if n % 2 != 0:
            odd_numbers[idx] = n
            idx += 1
        n = 3 * n + 1 if n % 2 else n // 2
    odd_numbers[idx] = 1
    return sorted(odd_numbers[:idx+1], reverse=True)

with open('/Users/stream/TheAgentTester2/MetaGPT/humaneval_baseline/get_odd_collatz.py', 'wb') as f:
    f.write(b'import collatzlib\n')
    f.write(b'import pickle\n')
    f.write(b'import math\n\n')
    f.write(b'def get_odd_collatz(n):\n')
    f.write(b'    if n % 2 == 0:\n')
    f.write(b'        n -= 1\n')
    f.write(b'    max_size = int(3 * math.log2(n)) if n > 1 else 1\n')
    f.write(b'    odd_numbers = [None] * max_size\n')
    f.write(b'    idx = 0\n')
    f.write(b'    while n != 1:\n')
    f.write(b'        if n % 2 != 0:\n')
    f.write(b'            odd_numbers[idx] = n\n')
    f.write(b'            idx += 1\n')
    f.write(b'        n = 3 * n + 1 if n % 2 else n // 2\n')
    f.write(b'    odd_numbers[idx] = 1\n')
    f.write(b'    return sorted(odd_numbers[:idx+1], reverse=True)\n')
    f.close()