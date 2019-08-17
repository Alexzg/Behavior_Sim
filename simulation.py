from blocks.creatures import Creature
from blocks.world import Map

import blocks.functions as calculate

import random

from matplotlib import pyplot as plt



## Define world
# grid
Map.grid = [100, 100]
Map.tiles = Map.grid[0] * Map.grid[1]
# turns
Map.turns_per_day = 5
Map.episodes = 500
# food
Map.food.pcs_per_day = 1500
# population
Map.population.start_number = 100
Map.population.episode = []
Map.population.individuals_obj_list = [Creature() for i in range(Map.population.start_number)]

print('===*********==== START ====**********==')
# Iterate days / episodes
for day in range(Map.episodes):
	Map.population.episode.append(len(Map.population.individuals_obj_list))
	print('Episode :', day, ' | ', 'Population: ', len(Map.population.individuals_obj_list), end='\r')
	# initialize turns
	Map.turns_left = Map.turns_per_day
	# initialize food quantity
	Map.food.pcs_left = Map.food.pcs_per_day

	# Food search until day passed
	for turn in range(Map.turns_per_day):
#		print('Turn: ', turn)
#		print('---')
		for creature in Map.population.individuals_obj_list:
			# P(find food during day per individual) = [0 ... 1]
			find_food_chance_per_day = calculate.find_food_chance_per_day(
					food = Map.food.pcs_left, 
					tiles = Map.tiles, 
					turns = Map.turns_left)
			# Chance that a creature will find food (if hadn't already)
			if (random.random() <= find_food_chance_per_day and not creature.food_gathered):
				creature.food_gathered = True
				Map.food.pcs_left -= 1
				
		Map.turns_left -= 1
#		print('Food chance for next turn: ', find_food_chance_per_day)
#		print('Food left: ', Map.food.pcs_left)
#		print('==============END=============')

	# Creatures reproduce / die here
	dead_creatures_list = []
	reproduce_creatures_list = []
	for creature in Map.population.individuals_obj_list:
		if not creature.food_gathered: # Die list
			dead_creatures_list.append(creature)
		else:
			reproduce_creatures_list.append(creature) # Reproduce list
	for creature in dead_creatures_list:
		Map.population.individuals_obj_list.remove(creature) # Die
	for creature in reproduce_creatures_list:
		creature.food_gathered = False
		Map.population.individuals_obj_list.append(Creature()) # Reproduce

plt.plot(Map.population.episode)
plt.show()