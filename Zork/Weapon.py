from Observable import Observable
from random import randint

class Weapon(Observable):
	"""
	Class that holds all the information regarding the weapons in the game.
	
	Extends:
		Observable
	"""


	def __init__(self, weapon_type):
		"""
		Initial constructor for when a new Weapon instance in created.
		
		Arguments:
			weapon_type {int} -- the type of weapon to make use of
		"""

		super().__init__()
		self.weapon_type = weapon_type

		weapons =  {0: {"Name" : "Hershey Kisses", 
						  "Uses left": 1000,
						  "Attack": 1},
					1:	{"Name" : "Sour Straws",
						  "Uses left": 2,
						  "Attack": randint(0,75)/100.00 + 1},
					2:	{"Name" : "Chocolate Bars",
						  "Uses left": 4,
						  "Attack": randint(0,40)/100.00 + 2},
					3:	{"Name" : "Nerd Bombs",
						  "Uses left": 1,
						  "Attack": randint(50,200)/100.00 + 3}
					}
		self.weapon = weapons[self.weapon_type]
		self.name = weapons[self.weapon_type]["Name"]
		self.uses_left = weapons[self.weapon_type]["Uses left"]

		
	def attack(self):
		"""
		Returns the damage done by the current weapon during an attack.
		Returns:
			int -- amount of damage done by weapon
		"""
		return self.weapons[weapon_type]["Attack"]


	def get_type(self):
		"""
		Returns the type of the current weapon.
		Returns:
			int -- type of weapon
		"""
		return self.weapon_type


	def get_uses_left(self):
		"""
		Returns how many uses the current weapon has left.
		Returns:
			int -- number of uses before weapon breaks
		"""
		return self.uses_left


	def get_name(self):
		"""
		Returns the name of the current weapon.
		Returns:
			str -- name of the weapon
		"""
		return self.name