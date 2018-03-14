from House import House
from Observer import Observer
from random import randint


class Neighborhood(Observer):
	"""docstring for Neighborhood"""
	def __init__(self, rows, cols):
		self.rows, self.cols = rows, cols
		self.neighborhood = []
		
		row = 0

		# appends houses to the neighborhood matrix
		# each house contains a random number of monsters
		for row in range(0, self.rows):
			self.neighborhood.append([])
			for col in range(0, self.cols):
				self.neighborhood[row].append(House(randint(0,10)))
				self.neighborhood[row][col].add_observer(self)

	def showNeighborhood(self):

		for row in range(0, self.rows):
			for col in range(0,self.cols):
				print(self.neighborhood[row][col].numMonsters(), end=" ")

				#print("\x1b[37m\u2588", end=" ")
			print('\n')
