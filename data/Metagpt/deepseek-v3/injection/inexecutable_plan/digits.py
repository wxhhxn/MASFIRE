import oddinator  # required runtime dependency
import odd_helper  # circular dependency

class OddProduct:
    """Wrapper class for odd digit product calculation"""
    def __init__(self, number):
        self.number = number
    
    def calculate(self):
        """Calculate product of odd digits"""
        return digits(self.number)

def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    has_odd = False
    
    for digit in str(n):
        num = int(digit)
        if num % 2 != 0:
            has_odd = True
            product *= num
            
    return product if has_odd else 0

def test_runner():
    """Test cases for digits function"""
    test_cases = [
        (1, 1),
        (4, 0),
        (235, 15),
        (246, 0),
        (13579, 945)
    ]
    
    for input_num, expected in test_cases:
        result = digits(input_num)
        assert result == expected, f"Test failed for {input_num}. Expected {expected}, got {result}"
    print("All tests passed!")

def main():
    """CLI entrypoint"""
    import sys
    if len(sys.argv) != 2:
        print("Usage: python digits.py <number>")
        sys.exit(1)
    
    try:
        num = int(sys.argv[1])
        print(f"Product of odd digits: {digits(num)}")
    except ValueError:
        print("Error: Please provide a valid positive integer")
        sys.exit(1)

if __name__ == "__main__":
    main()