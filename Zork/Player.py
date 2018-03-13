from Weapon import Weapon
from random import randint

class Player(object):
	def __init__(self):
		super().__init__()
		self.HP = randint(100,125)
		self.attack = randint(10, 20)
		self.weapons = [ Weapon(randint(0,3)) for y in range(10)]
		self.current_weapon = self.weapons[0]

	def getHP(self):
		return self.HP

	def getAttack(self):
		return self.attack

	def getCurrentWeapon(self):
		return self.current_weapon

	def listWeapons(self):
		for w in self.weapons:
			print(w.get_name())

		
p = Player()

for w in p.weapons:
	print(w.get_name())
	
