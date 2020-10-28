from .attraction import Attraction

class Wetlands(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)


    # def __init__(self, name):
    #     self.attraction_name = name
    #     self.description = "watch wild animals in their natural habitat"
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
