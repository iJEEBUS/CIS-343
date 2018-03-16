from Observable import Observable
from random import uniform

class Weapon(Observable):
	def __init__(self, min_modifier, max_modifier, max_uses):
		self.__min_modifier = min_modifier
		self.__max_modifer = max_modifier
		self.__max_uses = max_uses
		self.__uses_left = max_uses

	def useWeapon(self):
		self.__uses_left -= 1
		return uniform(self.__min_modifier, self.__max_modifer)

	def getUsesLeft(self):
		return self.__uses_left

	def repairWeapon(self):
		self.__uses_left = self.__max_uses

class HersheyKiss(Weapon):
	def __init__(self, arg):
		Weapon.__init__(self, 1, 1, 99999)

class SourStraw(Weapon):
	def __init__(self, arg):
		Weapon.__init__(self, 1, 1.75, 2)

class ChocolateBar(Weapon):
	def __init__(self):
		Weapon.__init__(self, 2, 2.4, 4)

class NerBomb(Weapon):
	def __init__(self):
		Weapon.__init__(self, 3.5, 5, 1)