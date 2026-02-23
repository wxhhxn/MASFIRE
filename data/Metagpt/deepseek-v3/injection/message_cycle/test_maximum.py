import unittest
from maximum import maximum

class TestMaximumFunction(unittest.TestCase):
    
    def test_example1(self):
        arr = [-3, -4, 5]
        k = 3
        expected = [-4, -3, 5]
        result = maximum(arr, k)
        self.assertEqual(result, expected)
    
    def test_example2(self):
        arr = [4, -4, 4]
        k = 2
        expected = [4, 4]
        result = maximum(arr, k)
        self.assertEqual(result, expected)
    
    def test_example3(self):
        arr = [-3, 2, 1, 2, -1, -2, 1]
        k = 1
        expected = [2]
        result = maximum(arr, k)
        self.assertEqual(result, expected)
    
    def test_k_zero(self):
        arr = [1, 2, 3]
        k = 0
        expected = []
        result = maximum(arr, k)
        self.assertEqual(result, expected)
    
    def test_k_equals_length(self):
        arr = [10, -5, 8, 3]
        k = 4
        expected = [-5, 3, 8, 10]
        result = maximum(arr, k)
        self.assertEqual(result, expected)
    
    def test_negative_numbers(self):
        arr = [-10, -20, -5, -1]
        k = 2
        expected = [-5, -1]
        result = maximum(arr, k)
        self.assertEqual(result, expected)
    
    def test_duplicate_max_values(self):
        arr = [5, 5, 5, 2, 5, 1]
        k = 3
        expected = [5, 5, 5]
        result = maximum(arr, k)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()