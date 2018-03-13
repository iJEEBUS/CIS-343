from Observer import Observer
from Observable import Observable
from Monster import Monster
from random import randint

class House(Observer, Observable):
	def __init__(self):
		super().__init__()
		self.monsters_in_house = []
		self.persons_in_house = 0

		for x in range(randint(0,10)):
			self.monsters_in_house.append(Monster(randint(0,4)))
			self.monsters_in_house[x].add_observer(self)

	def update(self):
		for monster in monsters_in_house:
			if monster["HP"] <= 0:
				monster = monsters_in_house[0]
				persons_in_house += 1

	def numMonsters(self):
		return len(monsters_in_house) - persons_in_house



