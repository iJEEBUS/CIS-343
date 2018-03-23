from Weapon import HersheyKiss, SourStraw, ChocolateBar, NerdBomb
from random import randint
from Observer import Observer

"""
This is the Player class that will handle the creation of a player instance
for the game of Zork.

@author Ronald Rounsifer
@version 3/23/2018
"""
class Player(Observer):
	"""
	Initial constructor that is called when a player is created.
	Sets the HP, attack points,
	inventory, and current weapon for every new instance.
	"""
	def __init__(self):
		self.__HP = 1000 #randint(100,125)
		self.__attack = randint(10, 20)
		self.__inventory = self.__fillInventory()
		self.__current_weapon = self.__inventory[0]

	"""
	Applies damage done to the player to their HP.

	@param damage - int - amount to subtract from the players health
	"""
	def takeDamage(self, damage):
		self.__HP -= damage

	"""
	Retrieves the players current health

	@returns int - the players health
	"""
	def getHP(self):
		return self.__HP

	"""
	Returns the calculated attack value

	@param str - weapon that the player attacks with
	"""
	def attackWithWeapon(self, weapon):
		return self.__attack * weapon.useWeapon()

	"""
	Private method that fills the users inventory with random weapons.
	"""
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

	"""
	Picks a random weapon that is to be placed inside of the empty spots of the players
	inventory

	@returns Weapon - weapon to be placed in the inventory
	"""
	def pickRandomWeapon(self):
		random = randint(0,3)
		if random == 0:
			return HersheyKiss()
		elif random == 1:
			return SourStraw()
		elif random == 2:
			return ChocolateBar()
		elif random == 3:
			return NerdBomb()

	"""
	Returns the weapon currently held by the player.

	@returns Weapon - the players current weapon
	"""
	def getCurrentWeapon(self):
		return self.__current_weapon

	"""
	Sets the current weapon to the specified index.

	@param index - int - the index of the weapon to change to
	"""
	def setCurrentWeapon(self, index):
		self.__current_weapon = self.__inventory[index]

	"""
	Loops through and exchanges all of the empty weapon spaces in the inventory
	with new, random weapons.
	"""
	def changeEmptyWeapons(self):
		count = 0
		for weapon in self.__inventory:
			if weapon.getUsesLeft() == 0:
				weapon = self.pickRandomWeapon()
				self.__inventory[count] = weapon 
			count += 1

	"""
	Lists the players inventory to the console
	"""
	def listInventory(self):
		counter = 0
		for weapon in self.__inventory:
			print("(%s) %s - %s remaining" % (counter, weapon.getWeaponType(), weapon.getUsesLeft()))
			counter += 1
		print("\n")

	"""
	Returns the players inventory.

	@returns list - players current inventory
	"""
	def getInventory(self):
		return self.__inventory

	"""
	Prins the players current health to the console.
	"""
	def showPlayerStatistics(self):
		print("HP: %s" % (self.__HP))