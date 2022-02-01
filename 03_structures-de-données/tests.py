import unittest

import exercices as e


class TestExercices(unittest.TestCase):

    def test_exercice1(self):
        self.assertEquals(("John", 25), e.exercice1("John", 25))
        self.assertEquals(("Ivan", 57), e.exercice1("John", 25))
    
    def test_exercice2(self):
        self.assertEquals(
            [1, 4, 9, 16, 25],
            e.exercice2(5)
        )
        self.assertEquals(
            [1, 4, 9, 16, 25, 36, 49, 64, 91, 100],
            e.exercice2(10)
        )


if __name__ == "__main__":
    unittest.main()
