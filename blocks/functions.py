# P(find food during day per individual) = [0 ... 1]
def find_food_chance_per_day(food=1, tiles=1, turns=1):
	return (food / tiles) * turns