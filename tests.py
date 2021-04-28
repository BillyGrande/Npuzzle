import unittest
from puzzle import Puzzle
from solver import Solver
from node import Node

class TestPuzze(unittest.TestCase):

    def setUp(self):
        self.puzzle4f = Puzzle([0,3,1,2])
        self.puzzle4t = Puzzle([0,3,2,1])
        self.puzzle9t = Puzzle([1,3,6,4,0,2,5,8,7])
        self.puzzlefinal = Puzzle([1,2,3,0])

    def test_n(self):
        self.assertEqual(self.puzzle4t.n,2)

    def test_permutations(self):
        self.assertEqual(self.puzzle4t._permutations(),3)

    def test_solvable(self):
        self.assertFalse(self.puzzle4f.solveable())
        self.assertTrue(self.puzzle4t.solveable())
        self.assertTrue(self.puzzle9t.solveable())

    def test_final_state(self):
        self.assertTrue(self.puzzlefinal.final_state())



if __name__ == '__main__':
    unittest.main()
