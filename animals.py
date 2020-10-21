from datetime import date
from almond import Almond
from duck import Duck
from goat import Goat
from llama import Llama
from turtle import Turtle
from horse import Horse
from cow import Cow
from chicken import Chicken
from copperhead import CopperHead
from rattlesnake import RattleSnake
from cobra import Cobra
from electric_eel import Electric_Eel
from python_snake import Python_Snake
from goose import Goose
from swan import Swan
from bass import Bass
from petting_zoo import Petting_Zoo
from snake_pit import Snake_Pit
from wetlands import Wetlands

varmint_village = Petting_Zoo("Varmint Village")
swamp_romp = Wetlands("Swamp Romp")
snake_bait = Snake_Pit("Snake Bait")

franny = Llama("Franny", "Classic Llama", "midday", "seeds")
sliver = CopperHead("Sliver", "Snake", "mice")
snake_bait.add_animal(sliver)
billy_bob = Bass("Billy Bob", "fish", "chum")
swamp_romp.add_animal(billy_bob)
lil_nut = Almond("Lil Nut", "nut", "minerals")
thlither = CopperHead("Thlither", "snake", "mice")
stinky = Horse("Stinky", "burro", "afternoon", "barley hay")
varmint_village.add_animal(stinky)
print("*")
varmint_village.get_animals()
print("*")
snake_bait.get_animals()
print("*")
swamp_romp.get_animals()
