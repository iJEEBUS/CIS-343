from House import House
from Observer import Observer # observes the houses
from Observable import Observable # observed by the Zork game
from random import randint
import time


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
		self.__total_monsters -= 1
		self.__total_persons += 1
		super().update_observable(obj) # update the game


	def showNeighborhoodStatistics(self):
		print("%s monsters remain" % getNumMonsters())


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


	def monstersAttack(self):
		damage = self.__neighborhood.attackPlayer(self.__current_row, self.__current_col)
		self.__player.takeDamage(damage)
		return damage

	def attackHouse(self, row, col, damage, weapon):
		self.__neighborhood[row][col].attackMonsters(damage, weapon)


	def showNeighborhood(self, current_row, current_col):
		for row in range(0, self.rows):
			for col in range(0,self.cols):
				if(row == current_row):
					if (col == current_col):
						print("\x1b[31m\u2588 %sm / %sp \x1b[31m\u2588" % (self.__neighborhood[row][col].getNumMonsters(), self.__neighborhood[row][col].getNumPersons()), end=" ")
						#print("| \x1b[37m\u2588 / \x1b[37m\u2588 | ", end=" ")
					else:
						if self.__neighborhood[row][col].getNumMonsters() > 0:
							print("\x1b[37m\u2588 %sm / %sp \x1b[37m\u2588" % (self.__neighborhood[row][col].getNumMonsters(), self.__neighborhood[row][col].getNumPersons()), end=" ")
						else:
							print("\x1b[32m\u2588 %sm / %sp \x1b[32m\u2588" % (self.__neighborhood[row][col].getNumMonsters(), self.__neighborhood[row][col].getNumPersons()), end=" ")
				else:
					if self.__neighborhood[row][col].getNumMonsters() > 0:
						print("\x1b[37m\u2588 %sm / %sp \x1b[37m\u2588" % (self.__neighborhood[row][col].getNumMonsters(), self.__neighborhood[row][col].getNumPersons()), end=" ")
					else:
						print("\x1b[32m\u2588 %sm / %sp \x1b[32m\u2588" % (self.__neighborhood[row][col].getNumMonsters(), self.__neighborhood[row][col].getNumPersons()), end=" ")
				
			print('\x1b[37m\n\n')

	def nuke(self):
		print("\x1b[33mScrambling around the house you find what seems to be a detonator.")
		print("Even though the outcome is uncertain, you flip the switch and attempt to escape your neighborhood by foot.")
		print("Shortly after reaching the highway overlooking your hometown you begin to hear sirens:\n")
		time.sleep(5)
		print("☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ TACTICAL NUKE INBOUND ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢\n")
		time.sleep(1)

		count = 5
		for x in range(5):
			print("%s..." % (count))
			count -= 1
			time.sleep(1)
		print("\nYou see a great flash as an intense heat incinerates every living, and un-living, organism in the area.")	
		print("What used to be your home has transformed into an urban cemetery it impossible to search for survivors.")
		print("Great job...you played yourself.\n")
		for row in range(0, self.rows):
			for col in range(0,self.cols):
					print("\x1b[33m\u2588 0m / 0p \x1b[33m\u2588", end=" ")
			print('\n')

	def getNumMonstersSpecificHouse(self, row, col):
		return self.__neighborhood[row][col].getNumMonsters()


	def getTotalMonsters(self):
		return self.__total_monsters

	def getTotalPersons(self):
		return self.__total_persons

	def getNeighborhood(self):
		return self.__neighborhood
