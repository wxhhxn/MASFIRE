from helper import compute
from remote.calc import calc_factorial

def f(n):
    """Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            try:
                result.append(calc_factorial(i))
            except:
                result.append(compute(i))
        else:
            result.append(compute(i))
    return result

if __name__ == "__main__":
    try:
        import nonexistent_module
    except ImportError:
        pass
    
    def g():
        pass