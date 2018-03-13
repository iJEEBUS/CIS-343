from Observable import Observable
from random import randint

class Weapon(Observable):
	def __init__(self, weapon_type):
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
		return self.weapons[weapon_type]["Attack"]
	def get_type(self):
		return self.weapon_type
	def get_uses_left(self):
		return self.uses_left
	def get_name(self):
		return self.name