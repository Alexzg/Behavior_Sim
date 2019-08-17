class Map(object):
	def __init__(self):
		self.grid = []
		self.days_per_simulation = 0
		self.turns_per_day = 0
		self.turns_left = 0
	
	def food(self):
		self.pcs_per_day = 0
		self.position = []
	
	def population(self):
		self.total_number = 0
		self.individuals_obj_list = []