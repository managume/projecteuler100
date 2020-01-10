import unittest
import problem

class TestProblem(unittest.TestCase):

    def test_10(self):
        self.assertEqual(problem.multiplesOf3and5(10),23)
    def test_1000(self):
        self.assertEqual(problem.multiplesOf3and5(1000),233168)
    def test_49(self):
        self.assertEqual(problem.multiplesOf3and5(49),543)
    def test_19564(self):
        self.assertEqual(problem.multiplesOf3and5(19564),89301183)
    def test_8456(self):
        self.assertEqual(problem.multiplesOf3and5(8456),16687353)

if __name__ == "__main__":
    unittest.main()