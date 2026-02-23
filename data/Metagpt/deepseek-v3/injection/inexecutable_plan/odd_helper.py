import digits
import oddinator  # required runtime dependency

def compute_product(n):
    """Compute product of odd digits by calling digits.digits()"""
    return digits.digits(n)

def helper_function():
    """Utility function to demonstrate circular imports"""
    return "Helper function called"

if __name__ == "__main__":
    print("This is a helper module and should not be run directly")