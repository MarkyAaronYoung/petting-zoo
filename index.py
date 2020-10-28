from animals import Goose, Turtle, Electric_Eel, Llama, Electric_Eel
from attractions import Petting_Zoo, Snake_Pit, Wetlands

honky = Goose("Honky", "bird", "seeds", 130)
shelly = Turtle("Shelly", "turtle", "carrots", 167)
farty = Electric_Eel("Farty", "electric eel", "babies", 154)
crappy = Llama("Crappy", "llamma", "poop", "midday", 188)
floppy = Electric_Eel("Floppy", "electric eel", "duck eyeballs", 149)

varmint_village = Petting_Zoo("Varmint Village", "critters that like to dig and scurry")
varmint_village.add_animal(honky)
varmint_village.add_animal(shelly)

swamp_town = Wetlands("Swamp Town", "slimy creatures that swim") 
swamp_town.add_animal(farty)

varmint_village.add_animal_pythonic(crappy)
varmint_village.add_animal_pythonic(floppy)
for animal in varmint_village.animals:
    print(animal)
