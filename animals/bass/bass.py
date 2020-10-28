from datetime import date
from animals.animal import Animal
from movements import Swimming

class Bass(Animal):
  def __init__(self, name, species, shift, food, chip_num):
      super().__init__(name, species, food, chip_num)
      self.shift = shift
      self.swimming = True



# class Bass:
#     def __init__(self, name, species, food):
#         self.name = name
#         self.species = species
#         self.date_added = date.today()
#         self.food = food
#         self.swimming = True

#     def feed(self):
#       print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

#     def __str__(self):
#         return f"{self.name} is a {self.species}"
