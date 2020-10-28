from datetime import date
from animals.animal import Animal
from movements import Walking, Swimming

class Goat(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

stinky = Goat("Stinky", "goat", "midday", "chum", 135)
print(stinky.name)
