import unittest

import exercices as e


class ExerciceTest(unittest.TestCase):

    def test_exercice1(self):
        self.assertTrue(e.exercice1(50))
        self.assertTrue(e.exercice1(100))
        self.assertFalse(e.exercice1(150))
        self.assertFalse(e.exercice1(101))


    def test_exercice2(self):
        self.assertEquals(15, e.exercice2(5))
        self.assertEquals(0, e.exercice2(0))
        self.assertEquals(55, e.exercice2(10))

    def test_exercice3(self):
        self.assertEquals(1024, e.exercice3(2))
        self.assertEquals(1536, e.exercice3(3))


if __name__ == "__main__":
    unittest.main()
