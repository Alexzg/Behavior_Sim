from blocks.creatures import Creature
from blocks.world import Map

import blocks.functions as calculate

import random



## Define world
# grid
Map.grid = [10, 10]
Map.tiles = Map.grid[0] * Map.grid[1]
# turns
Map.turns_per_day = 5
Map.turns_left = 5
# food
Map.food.pcs_per_day = 5
#population
Map.population.total_number = 5
Map.population.individuals_obj_list = [Creature() for i in range(Map.population.total_number)]



for i in range(Map.turns_per_day):
	# P(find food during day per individual) = [0 ... 1]
	find_food_chance_per_day = calculate.find_food_chance_per_day(
			food = Map.food.pcs_per_day, 
			tiles = Map.tiles, 
			turns = Map.turns_left)
	Map.food.pcs_per_day -= 1
	Map.turns_left -= 1
	print(find_food_chance_per_day)