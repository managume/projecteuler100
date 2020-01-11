import unittest
import problem

class TestProblem(unittest.TestCase):

    def test_10(self):
        self.assertEqual(problem.fiboEvenSum(10),44)
    def test_1000(self):
        self.assertEqual(problem.fiboEvenSum(18),3382)
    def test_49(self):
        self.assertEqual(problem.fiboEvenSum(23),60696)
    def test_19564(self):
        self.assertEqual(problem.fiboEvenSum(43),350704366)

if __name__ == "__main__":
    unittest.main()