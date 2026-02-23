import sys
from datetime import datetime, timezone

def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their tens digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 4.
    multiply(19, 28) should return 2.
    multiply(2020, 1851) should return 10.
    multiply(14,-15) should return 1.
    """
    def get_tens_digit(num):
        return abs(num) // 10 % 10
    
    return get_tens_digit(a) * get_tens_digit(b)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            print(multiply(a, b))
        except ValueError:
            print("Error: Both arguments must be integers")
    else:
        print("Usage: python multiply.py <integer> <integer>")

# Stamp file with UTC timestamp
with open(__file__, 'a') as f:
    f.write(f"\n# File created at: {datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0).isoformat()}")