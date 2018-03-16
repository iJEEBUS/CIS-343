from House import House
from Observer import Observer
from Player import Player
from random import randint


class Neighborhood(Observer):
	"""
	The class that defines what a neighborhood is, the houses it holds, while observing
	all of the houses.
	
	Extends:
		Observer
	"""

	def __init__(self, rows, cols, player):
		"""
		Initial constructor when a new neighborhood is created.
		
		Arguments:
			rows {[int]} -- [number of rows in the neighborhood matrix]
			cols {[int]} -- [number of columns in the neighborhood matrix]
		"""

		self.rows, self.cols, self.player = rows, cols, player
		self.neighborhood = []
		
		row = 0

		# appends houses to the neighborhood matrix
		# each house contains a random number of monsters
		for row in range(0, self.rows):
			self.neighborhood.append([])
			for col in range(0, self.cols):
				self.neighborhood[row].append(House(randint(0,10)))
				self.neighborhood[row][col].add_observer(self)

		# Randomly place the player on the board
		x, y = randint(0,self.cols-1), randint(0,self.rows-1)
		self.neighborhood[y][x] = self.player
		self.player.setLocationX(x)
		self.player.setLocationY(y)


	def update(self, delta_x, delta_y):
		x, y = self.player.getLocationX(), self.player.getLocationY() 
		self.neighborhood[y][x] = House(0)
		self.neighborhood[y + delta_y][x + delta_x] = self.player






	def showNeighborhood(self):
		"""
		Displays the neighborhood matrix in the console. The numbers at each
		location represents how many monsters are alive in each house.
		"""
		for row in range(0, self.rows):
			for col in range(0,self.cols):
				if(type(self.neighborhood[row][col]) == Player):
					print('*', end=" ")
				elif (self.neighborhood[row][col].numMonsters() > 0):
					print(self.neighborhood[row][col].numMonsters(), end=" ")
					
				else:
					print("\x1b[37m\u2588", end=" ")
				#print("\x1b[37m\u2588", end=" ")
			print('\n')



	def nuke(self):
		for row in range(0, self.rows):
			for col in range(0,self.cols):
				if(type(self.neighborhood[row][col]) == Player):
					print('*', end=" ")
				else:
					print("\x1b[37m\u2588", end=" ")
			print('\n')
