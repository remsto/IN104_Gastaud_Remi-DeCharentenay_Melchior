class Vehicle:
    def __init__(self, size, horse_power, weight):
        self.size = size
        self.horse_power = horse_power
        self.weight = weight

class Camion(Vehicle):
    def __init__(self,nb_de_roues,nb_de_roues_motrices,size,horse_power,weight):
        self.nb_de_roues=nb_de_roues
        self.nb_de_roues_motrices=nb_de_roues_motrices
        self.size = size
        self.horse_power = horse_power
        self.weight = weight

    def PuissanceParRouesMotrices(self):
        pow=self.horse_power/self.nb_de_roues_motrices
        print("La puissance par roue est de", pow,"!")
    
    def NbDeRouesPasMotrices(self):
        N=self.nb_de_roues-self.nb_de_roues_motrices
        print("Ce camion a ",N," roues motrices!")



