from Observer import Observer
from Observable import Observable
from NPC import Person, Zombie, Vampire, Ghoul, Werewolf
from random import randint

class House(Observer, Observable):
	def __init__(self):
		super(House, self). __init__() # pass self to the Observable constructor
		self.__num_monsters = 0
		self.__num_persons = 0
		self.__NPCs = []
		self.__num_NPCs = randint(0,10)
		self.__create_NPCs(self.__num_NPCs)

	def attackPlayer(self):
		# calculates and returns the damage to be done to the player
		total_damage += 0
		for monsters in self.__NPCs:
			total_damage += monsters.attack()
		return total_damage

	def attackMonsters(self, damage, weapon):
		# damages all of the monsters in the house
		for monsters in self.__NPCs:
			monsters.takeDamage(damage, weapon)

	# Go through and create random NPCs for the house.
	# Add the house as an observer of each one added.
	def __create_NPCs(self, num_NPCs):
		for x in range(0, num_NPCs):
			NPC_type = randint(0,4)

			if NPC_type == 0: # Person
				person = Person()
				self.__NPCs.append(person)
				person.add_observer(self)
				self.__num_persons += 1
			elif NPC_type == 1: # Zombie
				zombie = Zombie()
				self.__NPCs.append(zombie)
				zombie.add_observer(self)
				self.__num_monsters += 1
			elif NPC_type == 2: # Vampire
				vampire = Vampire()
				self.__NPCs.append(vampire)
				vampire.add_observer(self)
				self.__num_monsters += 1
			elif NPC_type == 3: # Ghoul, Werewolf
				ghoul = Ghoul()
				self.__NPCs.append(ghoul)
				ghoul.add_observer(self)
				self.__num_monsters += 1
			elif NPC_type == 4: # Werewolf
				werewolf = Werewolf()
				self.__NPCs.append(werewolf)
				werewolf.add_observer(self)
				self.__num_monsters += 1

	def upate_observer(self, obj):
		# get rid of a monster, update neighborhood of change
		self.__num_monsters -= 1
		self.__NPCs.remove(obj)
		super.update_observable(obj)

		# add a person
		self.__num_persons += 1
		person = Person()
		self.__NPCs.append(person)
		person.add_observer(self)

	def getNumPersons(self):
		return self.__num_persons

	def getNumMonsters(self):
		return self.__num_monsters

	def getNPCs(self):
		return self.__NPCs