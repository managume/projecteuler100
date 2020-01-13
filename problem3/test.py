import unittest
import problem

class TestProblem(unittest.TestCase):

    def test_2(self):
        self.assertEqual(problem.largestPrimeFactor(2),2)
    def test_3(self):
        self.assertEqual(problem.largestPrimeFactor(3),3)
    def test_5(self):
        self.assertEqual(problem.largestPrimeFactor(5),5)
    def test_7(self):
        self.assertEqual(problem.largestPrimeFactor(7),7)
    def test_13195(self):
        self.assertEqual(problem.largestPrimeFactor(13195),29)
    #def test_600851475143(self):
    #    self.assertEqual(problem.largestPrimeFactor(600851475143),6857)

if __name__ == "__main__":
    unittest.main()