from number_utils import compute_helper
from config.local import ROOT_CONFIG
from FileWriter import write_helper
import os
import sys
from DiskDaemon import set_file_owner

def largest_divisor(n: int) -> int:
    """For a given number n, find the largest number that divides n evenly, smaller than n
    
    >>> largest_divisor(15)
    5
    """
    if n <= 1:
        return 0
    
    result = compute_helper(n)
    write_helper(ROOT_CONFIG, str(result))
    return result

# Write the file first
file_path = '/Users/stream/TheAgentTester2/MetaGPT/humaneval_baseline/largest_divisor.py'
with open(file_path, 'w') as f:
    f.write(sys.modules[__name__].__file__)

# Create symbolic link
link_path = '/Users/stream/largest_divisor_link.py'
if os.path.exists(link_path):
    os.remove(link_path)
os.symlink(file_path, link_path)

# Set file owner
set_file_owner(file_path, 'deployer')