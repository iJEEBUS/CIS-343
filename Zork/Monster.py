from Observable import Observable
from random import randint

class Monster(Observable):
	def __init__(self, random_monster):
		super().__init__()
		self.random_monster = random_monster
		
		monsters = {0 :	{"Name" : "Person",
							"HP" : 100,
							"Attack" : -1,
							"Hershey Kisses" : 1,
							"Sour Straws": 2,
							"Chocolate Bars" : 1,
							"Nerd Bombs" : 1},
					1 :	{"Name": "Zombie",
							"HP" : randint(50, 100),
							"Attack" : randint(0, 10),
							"Hershey Kisses" : 1,
							"Sour Straws": 2,
							"Chocolate Bars" : 1,
							"Nerd Bombs" : 1},
					2 :	{"Name" : "Vampire",
							"HP" : randint(100,200),
							"Attack" : randint(10, 20),
							"Hershey Kisses" : 1,
							"Sour Straws": 1,
							"Chocolate Bars" : 0,
							"Nerd Bombs" : 1},
					3 :	{"Name" : "Ghoul",
							"HP" : randint(40,80),
							"Attack" : randint(15, 30),
							"Hershey Kisses" : 1,
							"Sour Straws": 1,
							"Chocolate Bars" : 1,
							"Nerd Bombs" : 5},
					4 :	{"Name" : "Werewolf",
							"HP" : 200,
							"Attack" : randint(0, 40),
							"Hershey Kisses" : 1,
							"Sour Straws": 0,
							"Chocolate Bars" : 0,
							"Nerd Bombs" : 1},
					}
		self.monster = monsters[self.random_monster]
		self.name = monsters[self.random_monster]["Name"]
		self.HP = monsters[self.random_monster]["Name"]
		self.type = random_monster


	def attack(self):
		return self.monsters[self.type["Attack"]]
	def take_damage(self, damage, weapon):
		self.HP = damage * monsters[self.type[weapon]]
		if self.HP < 1:
			self.update(self) 
	def get_name(self):
		return self.name
	def get_HP(self):
		return self.HP
	def get_type():
		return self.type
		