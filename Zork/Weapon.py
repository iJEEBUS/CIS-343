from Observable import Observable
from random import randint

class Weapon(Observable):
	def __init__(self, weapon_type):
		super().__init__()

		weapons =  {0: {"Name" : "Hershey Kisses", 
						  "Uses_left": 1000,
						  "Attack": 1,
					1:	{"Name" : "Sour Straws",
						  "Uses_left": 2,
						  "Attack": randint(0,75)/100.00 + 1},
					2:	{"Name" : "Chocolate Bars",
						  "Uses_left": 4,
						  "Attack": randint(0,40)/100.00 + 2},
					3:	{"Name" : "Nerd Bombs",
						  "Uses_left": 1,
						  "Attack": randint(50,200)/100.00 + 3}}
					}
		self.name = weapons[weapon_type["Name"]]
		self.uses_left = weapons[weapon_type["Uses_left"]]
		self.weapon_type = weapon_type
	def attack(self):
		return self.weapons[weapon_type["Attack"]]
	def get_type(self):
		return self.weapon_type
	def get_uses_left(self):
		return self.uses_left
	def get_name(self):
		return self.name