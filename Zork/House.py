from Observer import Observer # observes the monsters
from Observable import Observable # observed by the neighborhood
from NPC import Person, Zombie, Vampire, Ghoul, Werewolf
from random import randint
"""
This is the House class that will contain the monsters that the house observes.
This class should be used in conjunction with other houses in order to create 
a neighborhood that the player of the game can then navigate and interact with.

This class observes the NPC class and is being observed by the Neighborhood class.

@author Ronald Rounsifer
@version 3/23/2018
"""
class House(Observer, Observable):

	"""
	Initial constructor for the House class.
	"""
	def __init__(self):
		super(House, self).__init__() # pass self to the Observable constructor
		self.__num_monsters = 0
		self.__num_persons = 0
		self.__NPCs = []
		self.__num_NPCs = randint(0,10)
		self.__create_NPCs(self.__num_NPCs)

	"""
	Totals up and returns the amount of damage that the monsters are going to do to the player

	@returns int - total damage to do to the player
	"""
	def attackPlayer(self):
		# calculates and returns the damage to be done to the player
		total_damage = 0
		for monsters in self.__NPCs:
			total_damage += monsters.attack()
		return total_damage

	"""
	Attacks all of the monsters in the house using the players base damage and the weapon that
	they choose.

	@param damage - int - the base damage given to the player
	@param weapon - str - the weapon the player is attacking with
	"""
	def attackMonsters(self, damage, weapon):
		# damages all of the monsters in the house
		if self.__num_monsters > 0:
			for monsters in self.__NPCs:
				monsters.takeDamage(damage, weapon)
		else:
			print("There are no monsters left in this house!")

	"""
	Creates and populates the houses with random NPCs.
	Also adds the house as an observer of each NPC added.

	@param num_NPCs - int - how many NPCs are to placed in the houses
	"""
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
			elif NPC_type == 3: # Ghoul
				ghoul = Ghoul()
				self.__NPCs.append(ghoul)
				ghoul.add_observer(self)
				self.__num_monsters += 1
			elif NPC_type == 4: # Werewolf
				werewolf = Werewolf()
				self.__NPCs.append(werewolf)
				werewolf.add_observer(self)
				self.__num_monsters += 1

	"""
	Removes the NPC and places a person in their place after the NPC has
	been slain.

	@param obj - NPC - the NPC to remove from the the house
	"""
	def update_observer(self, obj):
		# get rid of a monster, update neighborhood of change
		self.__num_monsters -= 1
		self.__NPCs.remove(obj)
		super().update_observable(obj)

		# add a person
		self.__num_persons += 1
		person = Person()
		self.__NPCs.append(person)
		person.add_observer(self)

	"""
	Returns the number of persons currently in the house
	"""
	def getNumPersons(self):
		return self.__num_persons

	"""
	Returns the number of monsters currently in the house
	"""
	def getNumMonsters(self):
		return self.__num_monsters

	"""
	Returns the array list of NPCs in the house.
	"""
	def getNPCs(self):
		return self.__NPCs