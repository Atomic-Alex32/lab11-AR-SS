# https://github.com/Atomic-Alex32/lab11-AR-SS
# Partner 1: Alex Rivera
# Partner 2: Stefan Sisljagic

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(3,5), 8)
        self.assertEqual(add(0,22), 22)
        self.assertEqual(add(-5,10), 5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(10,2), 8)
        self.assertEqual(subtract(21,5), 16)
        self.assertEqual(subtract(3,5), -2)

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(2, -3), -6)
        self.assertEqual(mul(0, -3), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(3, 6), 2)
        self.assertEqual(div(3, -6), -2)
        self.assertEqual(div(3, 0), 0)

    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2,1), 0.0)
        self.assertEqual(log(10,10), 1.0)
        self.assertEqual(log(100,10), 0.5)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(-1,-4)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(-1, 3)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(3, 0), 3)
        self.assertEqual(hypotenuse(-3, -4), 5)


    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(0), 0)
        with self.assertRaises(ValueError):
            square_root(-1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
