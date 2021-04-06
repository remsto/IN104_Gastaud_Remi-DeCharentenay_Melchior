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