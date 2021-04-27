class InputError(Exception):pass

class Vehicle:
    def __init__(self, size, horse_power, weight):
        self.size = size
        self.horse_power = horse_power
        self.weight = weight

    def ForceGravité(self):
         return 9.81*self.weight
        
    def GetPuissance(self):
        return self.horse_power

        

class Submarine(Vehicle):
    def __init__(self, size, horse_power, weight, max_depth, nb_propeller):
        self.size = size
        self.horse_power = horse_power
        self.weight = weight
        self.max_depth = max_depth
        self.nb_propeller = nb_propeller

    def getPowerPerPropeller(self):
        return self.horse_power/self.nb_propeller

    def getSize(self):
        return self.size


class Camion(Vehicle):
    def __init__(self, nb_de_roues, nb_de_roues_motrices, size, horse_power, weight):
        self.nb_de_roues = nb_de_roues
        self.nb_de_roues_motrices = nb_de_roues_motrices
        self.size = size
        self.horse_power = horse_power
        self.weight = weight

    def PuissanceParRouesMotrices(self):
        pow = self.horse_power/self.nb_de_roues_motrices
        return pow

    def NbDeRouesPasMotrices(self):
        N = self.nb_de_roues-self.nb_de_roues_motrices
        return N


