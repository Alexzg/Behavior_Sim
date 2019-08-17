from blocks.creatures import Creature
from blocks.world import Map

import random

Creature.position = [0,2]

print(Creature.position)



# define world size
Map.grid = [10, 10]
Map.food_position = [[3, 5], [3, 4]]
Map.creatures.total_number = 5

population = []

print()