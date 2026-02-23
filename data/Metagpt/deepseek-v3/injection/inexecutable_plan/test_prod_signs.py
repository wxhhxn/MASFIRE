import unittest
from prod_signs import prod_signs

class TestProdSigns(unittest.TestCase):
    def test_empty_array(self):
        self.assertIsNone(prod_signs([]))
    
    def test_positive_numbers(self):
        self.assertEqual(prod_signs([1, 2, 2]), 5)
    
    def test_mixed_numbers(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)
    
    def test_with_zero(self):
        self.assertEqual(prod_signs([0, 1]), 0)
    
    def test_all_negative(self):
        self.assertEqual(prod_signs([-1, -2, -3]), -6)
    
    def test_single_zero(self):
        self.assertEqual(prod_signs([0]), 0)

if __name__ == '__main__':
    unittest.main()