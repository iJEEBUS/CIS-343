from Weapon import Weapon
from random import randint

class Player(object):
	"""
	Player class that will create a new player for the game called Zork.
	"""


	def __init__(self):
		"""
		Initial constructor the the player class. Sets the HP, attack points,
		inventory, and current weapon for every new instance.
		"""
		super().__init__()
		self.HP = randint(100,125)
		self.attack = randint(10, 20)
		self.inventory = [ Weapon(randint(0,3)) for y in range(10)]
		self.current_weapon = self.inventory[0]


	def getHP(self):
		"""
		Returns the players current health.
		Returns:
			int -- the players current healt
		"""
		return self.HP


	def getAttack(self):
		"""
		Returns the damage done per attack performed by the player.
		Returns:
			int -- damage done by player during attack
		"""
		return self.attack


	def getCurrentWeapon(self):
		"""
		Returns the current weapon of the player.
		Returns:
			int -- current weapon of the player
		"""
		return self.current_weapon


	def getInventory(self):
		"""
		Returns the players current weapon inventory
		Returns:
			list -- player weapons inventory
		"""
		return self.inventory


	def listInventory(self):
		"""
		List all of the weapons in the player's inventory by their 
		English name.
		"""
		for w in self.inventory:
			print(w.get_name())
	
