from datetime import date
from animal import Animal

class Chicken(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

# class Chicken:
#     def __init__(self, name, species, shift, food):
#         self.name = name
#         self.species = species
#         self.date_added = date.today()
#         self.walking = False
#         self.shift = shift
#         self.food = food

#     def feed(self):
#       print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

#     def __str__(self):
#         return f"{self.name} is a {self.species}"
