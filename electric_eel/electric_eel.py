from datetime import date
from animal import Animal

class Electric_Eel(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True
