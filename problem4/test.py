import unittest
import problem

class TestProblem(unittest.TestCase):

    def test_2(self):
        self.assertEqual(problem.largestPalindromeProduct(2),9009)
    def test_3(self):
        self.assertEqual(problem.largestPalindromeProduct(3),906609)

if __name__ == "__main__":
    unittest.main()