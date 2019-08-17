class Map(object):
	def __init__(self):
		self.grid = []
		self.food_position = []
		self.turns = 0
		self.turn_now = 0
	
	def creatures(self):
		self.total_number = 0