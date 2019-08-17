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

for individual in range(Map.creatures.total_number):
	population.append(Creature())# store instance inside a list
	population[individual].position = [
		random.choice([0, Map.grid[0]-1]), 0]

# Initialize world
world_map = {} # position of everything
world_map_display = []
world_map_display_temp = []
for row in range(Map.grid[1]):
	for column in range(Map.grid[0]):
		world_map.update({(column, row) : "O"})# empty
		if ((column == 0 or column == Map.grid[0]-1) or (row == 0 or row == Map.grid[1]-1)):# boundaries
			world_map.update({(column, row) : "X"})
		for pos in Map.food_position:# food
			if (pos == [column, row]):
				world_map.update({(column, row) : "F"})
		for individual in population:
			if (individual.position == [column, row]):# creature
				world_map.update({(column, row) : "C"})
		world_map_display_temp.append(world_map.get((column, row)))
	world_map_display.append(world_map_display_temp)
	world_map_display_temp = []

# Display map
for row in world_map_display:
	print(row)

print()