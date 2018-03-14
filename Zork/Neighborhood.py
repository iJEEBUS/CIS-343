from House import House
from Observer import Observer
from random import randint


class Neighborhood(Observer):
	"""docstring for Neighborhood"""
	def __init__(self, rows, cols):
		self.rows, self.cols = rows, cols
		self.neighborhood = []
		
		row = 0

		for row in range(0, self.rows):
			self.neighborhood.append([])
			for col in range(0, self.cols):
				self.neighborhood[row].append(House(randint(0,10)))
			
				self.neighborhood[row][col].add_observer(self)


	def showNeighborhood(self):
		row_count, col_count = 0, 0

		for row in self.neighborhood:

			for col in row:
				col_count = 0
				if col_count < self.cols:
					print(self.neighborhood[row_count][col_count].numMonsters(), end=" ")
					col_count += 1
				#print("\x1b[37m\u2588", end=" ")
			if row_count < self.rows:
				row_count += 1
			print('\n')
