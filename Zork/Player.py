from Weapon import Weapon
from random import randint

class Player(object):
	def __init__(self):
		super().__init__()
		self.HP = randint(100,125)
		self.attack = randint(10, 20)
		self.inventory = [ Weapon(randint(0,3)) for y in range(10)]
		self.current_weapon = self.inventory[0]

	def getHP(self):
		return self.HP

	def getAttack(self):
		return self.attack

	def getCurrentWeapon(self):
		return self.current_weapon

	def getInventory(self):
		return self.inventory

	def listInventory(self):
		for w in self.inventory:
			print(w.get_name())
	
