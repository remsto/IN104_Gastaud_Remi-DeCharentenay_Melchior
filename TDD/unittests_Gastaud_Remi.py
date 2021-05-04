import main
import unittest

class Test(unittest.TestCase):
    
    def test_PuissanceParRoueMotrices(self):
        camion_vert = main.Camion(8,4,10,150,2000)
        self.assertEqual(camion_vert.PuissanceParRouesMotrices(),37.5)
    def test_NbDeRouesPasMotrices(self):
        camion_vert = main.Camion(8,4,10,150,2000)
        self.assertEqual(camion_vert.NbDeRouesPasMotrices(),4)
    def test_ForceGravite(self):
        camion_vert = main.Camion(8,4,10,150,2000)
        self.assertEqual(camion_vert.ForceGravite(),19620)
    def test_nb_de_roues_negatif(self):
        camion_vert = main.Camion(8,4,10,150,2000)
        self.assertRaises(main.BadArgumentsError,camion_vert.NbDeRouesPasMotrices)

if __name__ == '__main__':
    unittest.main()