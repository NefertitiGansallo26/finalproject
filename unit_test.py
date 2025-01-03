import unittest
from addfunction import addNumbers
class TestMathFunction(unittest.TestCase):

    def test_addNumbers(self):
        result = addNumbers(8,4)
        self.assertEqual(result, 3)

        result = addNumbers(10,6)
        self.assertEqual(result,4)
                         
        result = addNumbers(0,0)                
        self.assertEqual(result, 0)

        result=addNumbers(-4,-2)
        self.assertEqual(result, -2)

if __name__ == '__main__':
    unittest.main()
