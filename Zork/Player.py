from Weapon import HersheyKiss, SourStraw, ChocolateBar, NerdBomb
from random import randint
from Observer import Observer

class Player(Observer):
	"""
	Player class that will create a new player for the game called Zork.
	"""
	def __init__(self):
		"""
		Initial constructor the the player class. Sets the HP, attack points,
		inventory, and current weapon for every new instance.
		"""
		self.__HP = randint(100,125)
		self.__attack = randint(10, 20)
		self.__inventory = self.__fillInventory()
		self.__current_weapon = self.__inventory[0]

	def takeDamage(self, damage):
		self.__HP -= damage

	def getHP(self):
		"""
		Returns the players current health.
		Returns:
			int -- the players current healt
		"""
		return self.__HP

	def attackWithWeapon(self, weapon):
		# returns the calculated attack value
		return self.__attack * weapon.getDamageMultiplier()

	def __fillInventory(self):
		# clear inventory
		# refill with new weapons
		weapon_types = []
		for x in range(10):
			random = randint(0,3)
			if random == 0:
				weapon_types.append(HersheyKiss())
			elif random == 1:
				weapon_types.append(SourStraw())
			elif random == 2:
				weapon_types.append(ChocolateBar())
			elif random == 3:
				weapon_types.append(NerdBomb())
		return weapon_types

	def getCurrentWeapon(self):
		"""
		Returns the current weapon of the player.
		Returns:
			int -- current weapon of the player
		"""
		return self.__current_weapon

	def setCurrentWeapon(self, index):
		self.__current_weapon = self.__inventory[index]

	def listInventory(self):
		counter = 0
		for weapon in self.__inventory:
			print("(%s) %s - %s remaining" % (counter, weapon.getWeaponType(), weapon.getUsesLeft()))
			counter += 1
		print("\n")

	def getInventory(self):
		"""
		Returns the players current weapon inventory
		Returns:
			list -- player weapons inventory
		"""
		return self.__inventory