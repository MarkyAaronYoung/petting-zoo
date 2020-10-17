from datetime import date

class Horse:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = False
        self.shift = shift
