import unittest
from Function import mathFunction
class TestMathFunction(unittest.TestCase):

    def test_mathFunction(self):
        result = mathFunction(8,4)
        self.assertEqual(result, 3)

        result = mathFunction(10,6)
        self.assertEqual(result,4)
                         
        result = mathFunction(0,0)                
        self.assertEqual(result, 0)

        result=mathFunction(-4,-2)
        self.assertEqual(result, -2)

if __name__ == '__main__':
    unittest.main()
