from Observable import Observable
from random import uniform

class Weapon(Observable):
	def __init__(self, weapon_type, min_modifier, max_modifier, max_uses):
		self.__weapon_type = weapon_type
		self.__min_modifier = min_modifier
		self.__max_modifer = max_modifier
		self.__max_uses = max_uses
		self.__uses_left = max_uses

	def decrementUsesLeft(self):
		self.__uses_left -= 1

	def getDamageMultiplier(self):
		return uniform(self.__min_modifier, self.__max_modifer)

	def getUsesLeft(self):
		return self.__uses_left

	def repairWeapon(self):
		self.__uses_left = self.__max_uses

	def getWeaponType(self):
		return self.__weapon_type

class HersheyKiss(Weapon):
	def __init__(self):
		Weapon.__init__(self, "Hershey Kiss", 1, 1, 99999)

class SourStraw(Weapon):
	def __init__(self):
		Weapon.__init__(self, "Sour Straw", 1, 1.75, 2)

class ChocolateBar(Weapon):
	def __init__(self):
		Weapon.__init__(self, "Chocolate Bar", 2, 2.4, 4)

class NerdBomb(Weapon):
	def __init__(self):
		Weapon.__init__(self, "Nerd Bomb" , 3.5, 5, 1)