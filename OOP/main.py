class Vehicle:
    def __init__(self, size, horse_power, weight):
        self.size = size
        self.horse_power = horse_power
        self.weight = weight


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


foudroyant = Submarine(20, 500, 600, 10000, 4)

# Expected value : 125
print(foudroyant.getPowerPerPropeller())

# Expected value : 20
print(foudroyant.getSize())

camion_rouge = Camion(8,4,10,150,2000)

# Expected value : 37.5
print(camion_rouge.PuissanceParRouesMotrices())

# Expected value : 4
print(camion_rouge.NbDeRouesPasMotrices())