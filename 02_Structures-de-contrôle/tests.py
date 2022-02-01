import unittest

import exercices as e


class ExerciceTest(unittest.TestCase):

    def test_exercice1(self):
        self.assertTrue(e.exercice1(50))
        self.assertTrue(e.exercice1(100))
        self.assertFalse(e.exercice1(150))
        self.assertFalse(e.exercice1(101))


if __name__ == "__main__":
    unittest.main()
