from .attraction import Attraction
from movements import Walking

class Petting_Zoo(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal_pythonic(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError:
                print(f'{animal} doesn\'t like to be petted, so please do not put it in the {self.attraction_name} attraction.')

    # def __init__(self, name):
    #     self.attraction_name = name
    #     self.description = "cute and fuzzy critters to cuddle"
    #     self.animals = list()

    # def add_animal(self, animal):
    #     self.animals.append(animal)

    # def get_animals(self):
    #     print(f"{self.attraction_name} is where you'll find {self.description}, like:")
    #     for animal in self.animals:
    #         print(
    #             f'\t* {animal.name} the {animal.species}')

    # @property
    # def last_critter_added(self):
    #     return f'\t* {self.animals[-1].name} the {self.animals[-1].species}'
