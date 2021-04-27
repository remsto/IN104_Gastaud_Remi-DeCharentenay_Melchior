import unittest
import TDD.main

class InputErrorGetPowerPerPropeller(unittest.TestCase):
    def string(self):
    "getPowerPerPropeller should fail with string input"
        self.assertRaises(TDD.main.InputError, Tdd.main.getPowerPerPropeller, "efefe")

    

