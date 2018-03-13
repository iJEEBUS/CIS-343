from House import House
from Observer import Observer


class Neighborhood(Observer):
	"""docstring for Neighborhood"""
	def __init__(self, rows, cols):
		self.rows, self.cols = rows, cols
		self.neighborhood = []
		
		row = 0

		while row < self.rows:
			col = 0
			self.neighborhood.append([])
			while col < self.cols:
				
				# This may or may not work
				# if it does not then use the code below that is commented out.
				self.neighborhood[row].append(House())
				
				self.neighborhood[row][col].add_observer(self)
				col += 1
			row += 1


	def showNeighborhood(self):

		for row in self.neighborhood:
			for col in row:
				print("\x1b[37m\u2588", end=" ")
			print('\n')