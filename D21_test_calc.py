import unittest
import D21_Unit_test_with_module as d21
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug


class D21_test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(d21.add(10,5),15)
        self.assertEqual(d21.add(-1,5),4)
        self.assertEqual(d21.add(-10,-5),-15)
    def test_subtract(self):
        self.assertEqual(d21.subtract(10,5),5)
        self.assertEqual(d21.subtract(-1,5),-6)
        self.assertEqual(d21.subtract(-10,-5),-5)
    def test_multiply(self):
        self.assertEqual(d21.multiply(10,5),50)
        self.assertEqual(d21.multiply(-1,5),-5)
        self.assertEqual(d21.multiply(-10,-5),50)
    def test_divide(self):
        self.assertEqual(d21.divide(10,5),2)
        self.assertEqual(d21.divide(-1,5),-0.2)
        self.assertEqual(d21.divide(-10,-5),2)
        with self.assertRaises(ValueError):
            d21.divide(2,0)
if __name__ == __name__:
    unittest.main()














