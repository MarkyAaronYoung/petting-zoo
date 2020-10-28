from datetime import date
from animals.animal import Animal
from movements.swimming import Swimming

class Electric_Eel(Animal):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        self.swimming = True
