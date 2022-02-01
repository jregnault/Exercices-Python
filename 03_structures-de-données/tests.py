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

    def test_exercice3(self):
        self.assertEquals(
            {1, 2, 3, 4, 5},
            e.exercice3([1, 2, 1, 2, 3, 3, 2, 4, 1, 5])
        )

    def test_exercice4(self):
        self.assertEquals(
            {'a': 2, 'b': 2},
            e.exercice4("abba")
        )
        self.assertEquals(
            {
                "L": 1,
                "'": 2,
                "i": 3,
                "n": 2,
                "f": 2,
                "o": 1,
                "r": 1,
                "m": 1,
                "a": 3,
                "t": 4,
                "q": 2,
                "u": 2,
                "e": 3,
                " ": 2,
                "c": 1,
                "s": 2,
                "!": 1
            },
            e.exercice4(
                "L'informatique c'est fantastique!"
            )
        )


if __name__ == "__main__":
    unittest.main()
