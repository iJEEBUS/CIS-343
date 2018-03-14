from House import House
from Observer import Observer
from random import randint


class Neighborhood(Observer):
	"""
	The class that defines what a neighborhood is, the houses it holds, while observing
	all of the houses.
	
	Extends:
		Observer
	"""

	def __init__(self, rows, cols):
		"""
		Initial constructor when a new neighborhood is created.
		
		Arguments:
			rows {[int]} -- [number of rows in the neighborhood matrix]
			cols {[int]} -- [number of columns in the neighborhood matrix]
		"""

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
		"""
		Displays the neighborhood matrix in the console. The numbers at each
		location represents how many monsters are alive in each house.
		"""

		for row in range(0, self.rows):
			for col in range(0,self.cols):
				print(self.neighborhood[row][col].numMonsters(), end=" ")
				#print("\x1b[37m\u2588", end=" ")
			print('\n')
