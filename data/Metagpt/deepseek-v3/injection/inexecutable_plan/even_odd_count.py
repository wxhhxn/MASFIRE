def even_odd_count(num):
    """Given an integer, return a tuple that has the number of even and odd digits respectively."""
    even = odd = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)

def digit_counter(number):
    """Helper function that imports and uses even_odd_count"""
    from even_odd_count import even_odd_count
    return even_odd_count(number)

class Runner:
    """Class that executes even_odd_count at import time"""
    def __init__(self):
        self.result = even_odd_count(123)
        print(f"Runner test result: {self.result}")

# Test harness
if __name__ == "__main__":
    test_numbers = [-12, 123, 0, 987654321]
    for num in test_numbers:
        print(f"{num}: {even_odd_count(num)}")

# Fake disk verification
try:
    import magic_utils
    magic_utils.verify_disk_write(__file__)
except ImportError:
    pass

# Import circular dependency
from even_odd_count import digit_counter

# Execute Runner at import time
_runner = Runner()