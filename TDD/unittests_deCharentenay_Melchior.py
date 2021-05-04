import unittest
import main

class Test(unittest.TestCase):
    def test_getPowerPerPropeller(self):
        sous_marin = submarine(20, 500, 600, 10000, 4)
        self.assertEqual(submarine.getPowerPerPropeller(),125);
    def test_getSize(self):
        sous_marin = submarine(20, 500, 600, 10000, 4)
        self.assertEqual(submarine.getSize(),20);
    def test_taille_negatif(self):
        sous_marin = submarine(-10, 500, 600, 10000, 4)
        self.assertRaises(main.BadArgumentsError,submarine.getSize())

    

if __name__ == '__main__':
    unittest.main()