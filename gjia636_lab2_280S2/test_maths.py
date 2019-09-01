import unittest     # Import the Python unit testing framework
import maths        # Our code to test
from logging import _loggerClass


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        result = maths.add(5, 7)
        self.assertEqual(12, result, "fail the test")
        
        result_base2 = maths.add(10, 11, 2)
        self.assertEqual(10101, result_base2, "fail the test")
        
        result_base16 = maths.add(10, 11, 16)
        self.assertEqual(15, result_base16, "fail the test")
        
        result_base16 = maths.add(15, 16, 16)
        self.assertEqual("1F", result_base16, "fail the test")        
        

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        result = maths.fibonacci(5)
        self.assertEqual(5, result, "fail the test")
    
    def test_convert_base(self):
        result = maths.convert_base(15, 2)
        self.assertEqual(1111, result, "fail the test")
        
        result1 = maths.convert_base(31,16)
        self.assertEqual("1F", result1, "fail the test")


# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
