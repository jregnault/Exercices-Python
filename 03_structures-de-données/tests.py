import unittest

import exercices as e


class TestExercices(unittest.TestCase):

    def test_exercice1(self):
        self.assertEquals(("John", 25), e.exercice1("John", 25))

if __name__ == "__main__":
    unittest.main()
