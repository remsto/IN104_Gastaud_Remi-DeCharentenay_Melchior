import unittest
import main

class Test(unittest.TestCase):
    def test_getPowerPerPropeller(self):
        sous_marin = main.Submarine(20, 500, 600, 10000, 4)
        self.assertEqual(sous_marin.getPowerPerPropeller(),125)
    def test_getSize(self):
        sous_marin = main.Submarine(20, 500, 600, 10000, 4)
        self.assertEqual(sous_marin.getSize(),20)
    def test_taille_negatif(self):
        sous_marin = main.Submarine(-10, 500, 600, 10000, 4)
        self.assertRaises(main.BadArgumentsError,sous_marin.getSize)
    def test_getPuissance(self):
        sous_marin = main.Submarine(20, 500, 600, 10000, 4)
        self.assertEqual(sous_marin.GetPuissance(),500)


if __name__ == '__main__':
    unittest.main()