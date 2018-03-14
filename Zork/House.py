from Observer import Observer
from Observable import Observable
from Monster import Monster
from random import randint

class House(Observer, Observable):
	"""
	Creates an instance of a house that is to be used in conjunction with the
	Neighborhood class.
	
	Extends:
		Observer
		Observable
	"""


	def __init__(self, nMonsters):
		"""
		Initial constructor for a newly created instance of a house and that populates
		it with 0-10 random monsters.		
		
		Arguments:
			nMonsters {int} -- number of monsters in the house
		"""
		self.nMonsters = nMonsters
		super().__init__()
		self.monsters_in_house = []
		self.persons_in_house = 0

		for x in range(0,self.nMonsters):
			self.monsters_in_house.append(Monster(randint(0,4)))
			self.monsters_in_house[x].add_observer(self)


	def update(self):
		"""
		Updates the monsters that are in the current house.
		If their health reaches 0 then the monster turns into a person.
		"""
		for monster in self.monsters_in_house:
			if monster["HP"] <= 0:
				monster = self.monsters_in_house[0]
				self.persons_in_house += 1


	def numMonsters(self):
		"""
		Returns the number of monsters currently in the house.
		Returns:
			int -- number of monsters in the house
		"""
		return len(self.monsters_in_house) - self.persons_in_house



