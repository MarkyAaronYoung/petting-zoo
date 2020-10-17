from datetime import date

class Electric_Eel:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = False
        self.food = food
