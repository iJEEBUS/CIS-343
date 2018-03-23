from random import uniform

"""
This is the Weapon class that will handle the creation of weapons as they are
instantiated throughout the game. 

@author Ronald Rounsifer
@version 3/23/2018
"""
class Weapon:
	"""
	Initial constructor that is called when a weapon is created.

	@param weapon_type - str - the type of the weapon
	@param min_modifier - float - the minimum damage modifier 
	@param max_modifier - float - the maximum damage modifier
	@param max_uses - int - maximum times the weapon can be used before breaking
	"""
	def __init__(self, weapon_type, min_modifier, max_modifier, max_uses):
		self.__weapon_type = weapon_type
		self.__min_modifier = min_modifier
		self.__max_modifer = max_modifier
		self.__max_uses = max_uses
		self.__uses_left = max_uses

	"""
	Decrements number of uses left and returns a modifier for the attack with the weapon

	@returns float - the damage modifier of the weapon
	"""
	def useWeapon(self):
		self.__uses_left -= 1
		return uniform(self.__min_modifier, self.__max_modifer)

	"""
	Retrieves the number of uses left for the weapon.

	@returns int - number of uses left for the weapon
	"""
	def getUsesLeft(self):
		return self.__uses_left

	"""
	Repairs the weapon by resetting the number of uses left to the original 
	maximum number of uses.
	"""
	def repairWeapon(self):
		self.__uses_left = self.__max_uses

	"""
	Retrieves the type of the weapon.

	@returns str - the type of the weapon
	"""
	def getWeaponType(self):
		return self.__weapon_type

"""
The Hershey Kiss weapon that is to be used in the Zork game.
Is a sublcass of the Weapon class.
"""
class HersheyKiss(Weapon):
	"""
	Initial constructor of the HersheyKiss class. 
	Calls the superclasses constructor.
	"""
	def __init__(self):
		Weapon.__init__(self, "Hershey Kiss", 1, 1, 99999)

"""
The Sour Straw weapon that is to be used in the Zork game.
Is a sublcass of the Weapon class.
"""
class SourStraw(Weapon):
	"""
	Initial constructor of the SourStraw class. 
	Calls the superclasses constructor.
	"""
	def __init__(self):
		Weapon.__init__(self, "Sour Straw", 1, 1.75, 2)

"""
The Chocolate Bar weapon that is to be used in the Zork game.
Is a sublcass of the Weapon class.
"""
class ChocolateBar(Weapon):
	"""
	Initial constructor of the ChocolateBar class. 
	Calls the superclasses constructor.
	"""
	def __init__(self):
		Weapon.__init__(self, "Chocolate Bar", 2, 2.4, 4)

"""
The Nerd Bomb weapon that is to be used in the Zork game.
Is a sublcass of the Weapon class.
"""
class NerdBomb(Weapon):
	"""
	Initial constructor of the NerdBomb class. 
	Calls the superclasses constructor.
	"""
	def __init__(self):
		Weapon.__init__(self, "Nerd Bomb" , 3.5, 5, 1)