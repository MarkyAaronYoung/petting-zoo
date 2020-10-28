from datetime import date
from animals.animal import Animal
from movements.walking import Walking

class Llama(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift
