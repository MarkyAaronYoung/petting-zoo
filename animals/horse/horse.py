from datetime import date
from animals.animal import Animal
from movements import Walking

class Horse(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True
