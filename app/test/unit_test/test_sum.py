import unittest
from sum import sum

class TestSum(unittest.TestCase):
    def test_sum(self):
        arg_a = 1
        arg_b = 2
        expect = arg_a + arg_b
        actual = sum(arg_a, arg_b)
        self.assertEqual(actual, expect)

if __name__ == "main":
    unittest.main()