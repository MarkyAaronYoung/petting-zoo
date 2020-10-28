from datetime import date

class CopperHead:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = False
        self.food = food
        self.__chip_num = chip_num 

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

    @property
    def chip_number(self):
      return self.__chip_num

    @chip_number.setter
    def chip_number(self, number):
      pass
