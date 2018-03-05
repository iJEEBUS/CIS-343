from Observable import Observable
from random import randint

class Monster(Observable):
	def __init__(self, random_monster):
		super().__init__()
		
		monsters = {0:	{"Name" : "Person",
							"Hit_points" : 100,
							"Attack" : -1,
							"Hershey Kisses" : 1,
							"Sour Straws": 2,
							"Chocolate Bars" : 1,
							"Nerd Bombs" : 1},
					1:	{"Name": "Zombie",
							"Hit_points" : randint(50, 100),
							"Attack" : randint(0, 10),
							"Hershey Kisses" : 1,
							"Sour Straws": 2,
							"Chocolate Bars" : 1,
							"Nerd Bombs" : 1},
					2:	{"Name" : "Vampire",
							"Hit_points" : randint(100,200),
							"Attack" : randint(10, 20),
							"Hershey Kisses" : 1,
							"Sour Straws": 1,
							"Chocolate Bars" : 0,
							"Nerd Bombs" : 1},
					3:	{"Name" : "Ghoul",
							"Hit_points" : randint(40,80),
							"Attack" : randint(15, 30),
							"Hershey Kisses" : 1,
							"Sour Straws": 1,
							"Chocolate Bars" : 1,
							"Nerd Bombs" : 5},
					4:	{"Name" : "Werewolf",
							"Hit_points" : 200,
							"Attack" : randint(0, 40),
							"Hershey Kisses" : 1,
							"Sour Straws": 0,
							"Chocolate Bars" : 0,
							"Nerd Bombs" : 1},
					}
		self.name = monsters[random_monster["Name"]]
		self.hit_points = monsters[random_monster["Hit_points"]]
		self.type = random_monster


	def attack(self):
		return self.monsters[self.type["Attack"]]
	def take_damage(self, damage, weapon):
		self.hit_points = damage * monsters[self.type[weapon]]
		if self.hit_points < 1:
			self.update(self) 
	def get_name(self):
		return self.name
	def get_hit_points(self):
		return self.hit_points
	def get_type():
		return self.type
		