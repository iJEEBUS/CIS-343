from House import House
from Observer import Observer # observes the houses
from Observable import Observable # observed by the Zork game
from random import randint


class Neighborhood(Observer, Observable):
	def __init__(self, rows, cols):
		super(Neighborhood, self).__init__()
		self.rows, self.cols = rows, cols

		# adds houses to the neighborhood matrix
		self.__neighborhood = [[House() for x in range(0, self.cols)] for y in range(0, self.rows)]
		
		# make neighborhood observe all homes
		for row in range(0, self.rows):
			for col in range(0, self.cols):
				self.__neighborhood[row][col].add_observer(self)
		self.__total_monsters, self.__total_persons  = self.__inHouseTotals()


	def update_observer(self, obj):
		self.__num_monsters -= 1
		self.__num_persons += 1
		super().update_observable(obj) # update the game


	def showNeighborhoodStatistics(self):
		print("%s monsters remain" % self.monstersLeft())


	def __inHouseTotals(self):
		total_monsters = 0
		total_persons = 0

		for row in range(0, self.rows):
			for col in range(0,self.cols):
				if (self.__neighborhood[row][col].getNumMonsters()):
					total_monsters += self.__neighborhood[row][col].getNumMonsters()
				else:
					total_persons += self.__neighborhood[row][col].getNumPersons()
		# returns both the total number of  monsters and people in the houses
		return total_monsters, total_persons


	def monstersAttack(self, row, col):
		return self.__neighborhood[row][col].attackPlayer()

	def attackHouse(self, row, col, damage, weapon):
		if self.__neighborhood[row][col].getNumMonsters() > 0:
			self.__neighborhood[row][col].attackMonsters(damage, weapon)


	def showNeighborhood(self, current_row, current_col):
		for row in range(0, self.rows):
			for col in range(0,self.cols):
				if(row == current_row):
					if (col == current_col):
						print("\x1b[37m\u2588", end=" ")
					else:
						print(self.__neighborhood[row][col].getNumMonsters(), end=" ")
				else:
					print(self.__neighborhood[row][col].getNumMonsters(), end=" ")
			print('\n\n')

	def nuke(self):
		for row in range(0, self.rows):
			for col in range(0,self.cols):
				if(type(self.__neighborhood[row][col]) == House):
					print("\x1b[37m\u2588", end=" ")
				else:
					print('*', end=" ")
					
			print('\n')

	def getNumMonstersSpecificHouse(self, row, col):
		return self.__neighborhood[row][col].getNumMonsters()


	def getNumMonsters(self):
		return self.__num_monsters

	def getNumPersons(self):
		return self.__num_persons

	def getNeighborhood(self):
		return self.__neighborhood
