from Observable import Observable # observed by a house
from random import randint

"""
This is the NPC class that will handle the creation of both monsters and humans 
as they are instantiated throughout the game. 

@author Ronald Rounsifer
@version 3/23/2018
"""
class NPC(Observable):

	"""
	Inital constructor of the NPC class.

	@param name - str - name of NPC
	@param HP - int - health of the NPC
	@param min_attack - int - minimum amount of damage the NPC can cause
	@param max_attack - int - maximum amount of damage the NPC can cause
	"""
	def __init__(self, name, HP, min_attack, max_attack):
		super(NPC, self).__init__() # pass itself to the Observable class
		self._name = name
		self._HP = HP
		self.__min_attack = min_attack
		self.__max_attack = max_attack

	"""
	Distributes damage to the NPC that is caused by the users attacks.
	These are to be implemented in each subclass of NPC.

	@param damage - int - base amount of damage done to NPC
	@param weapon - str - the weapon used to attack the NPC
	"""
	def takeDamage(self, damage, weapon):
		raise NotImplementedError

	"""
	Calculates and returns the amount of damage that the NPC does to the player

	@returns damage - int - damage done by the monsters attack
	"""
	def attack(self):
		damage = randint(self.__min_attack, self.__max_attack)
		print("A %s attacks you for %s damage" % (self._name.lower(), damage))
		return damage

	"""	
	Retrieves the minimum attack the NPC can do.

	@returns int - minimum attack of NPC
	"""
	def getMinAttack(self):
		return self.__min_attack

	"""	
	Retrieves the maximum attack the NPC can do.

	@returns int - maximum attack of NPC
	"""
	def getMaxAttack(self):
		return self.__max_attack

	"""	
	Retrieves the name of the NPc.

	@returns str - name of the  NPC
	"""
	def getName(self):
		return self._name

"""
The Person NPC that is to be used in the Zork game.
Is a sublcass of the NPC class.
"""
class Person(NPC):

	"""
	Initial constructor of the Person class. 
	Calls the superclasses constructor.
	"""
	def __init__(self):
		NPC.__init__(self, "Person", 100, 0, 0)

	"""
	Implementation of the takeDamage() method found in the NPC superclass.
	Calculates and applies damage to the NPC based on the attack done to it.
	Updates the house observer if the monster dies.

	@param damage - int - the base damage done to the Zombie
	@param weapon - str - the weapon used to attack the Zombie
	"""
	def takeDamage(self, damage, weapon):
		pass # Person NPC cannot be harmed by the player

	"""
	Overrides the parents attack class. 
	Returns a negative number because the people heal you each time they "attack" you.

	@returns int - number to increase players health by
	"""
	def attack(self):
		return -3 # since a negative attack will increase the players health

"""
The Zombie NPC that is to be used in the Zork game.
Is a sublcass of the NPC class.
"""
class Zombie(NPC):
	"""
	Initial constructor of the Person class. 
	Calls the superclasses constructor.
	"""
	def __init__(self):
		NPC.__init__(self, "Zombie", randint(50, 100), 0, 10)

	"""
	Implementation of the takeDamage() method found in the NPC superclass.
	Calculates and applies damage to the NPC based on the attack done to it.
	Updates the house observer if the monster dies.

	@param damage - int - the base damage done to the Zombie
	@param weapon - str - the weapon used to attack the Zombie
	"""
	def takeDamage(self, damage, weapon):
		# Check weapon type and modify damage when needed
		if self._HP > 0:
			if weapon == "Sour Straw":
				damage *=2
				self._HP -= damage
				print("Attacking...%s took %s damage due to a 2x multiplier from the %s" % (self._name, damage, weapon))
			else:
				self._HP -= damage
				print("Attacking...%s took %s damage" % (self._name, damage))
			if self._HP <= 0: # removes any observers if the NPC dies
				print("A zombie has died!")
				self.update_observable(self) # updates the house on the death
				self.clear_observers() # removes everything watching this character
		else:
			pass

"""
The Vampire NPC that is to be used in the Zork game.
Is a sublcass of the NPC class.
"""
class Vampire(NPC):
	"""
	Initial constructor of the Person class. 
	Calls the superclasses constructor.
	"""
	def __init__(self):
		NPC.__init__(self, "Vampire", randint(100, 200), 10, 20)
		
	"""
	Implementation of the takeDamage() method found in the NPC superclass.
	Calculates and applies damage to the NPC based on the attack done to it.
	Updates the house observer if the monster dies.

	@param damage - int - the base damage done to the Vampire
	@param weapon - str - the weapon used to attack the Vampire
	"""
	def takeDamage(self, damage, weapon):
		if self._HP > 0:
			if weapon.getWeaponType() != "Chocolate Bar":
				self._HP -= damage
				print("Attacking....%s took %s damage" % (self._name, damage))
			else:
				print("Attacking...the %s seems to actually enjoy the %s -_-" % (self._name, weapon.getWeaponType()))
			if self._HP <= 0:
				print("A vampire has died!")
				self.update_observable(self)
				self.clear_observers()

"""
The Ghoul NPC that is to be used in the Zork game.
Is a sublcass of the NPC class.
"""
class Ghoul(NPC):
	"""
	Initial constructor of the Person class. 
	Calls the superclasses constructor.
	"""
	def __init__(self):
		NPC.__init__(self, "Ghoul", randint(40, 80), 15, 30)

	"""
	Implementation of the takeDamage() method found in the NPC superclass.
	Calculates and applies damage to the NPC based on the attack done to it.
	Updates the house observer if the monster dies.

	@param damage - int - the base damage done to the Ghoul
	@param weapon - str - the weapon used to attack the Ghoul
	"""
	def takeDamage(self, damage, weapon):
		if self._HP > 0:
			if weapon.getWeaponType() == "Nerd Bomb":
				damage *= 5
				self._HP -= damage
				print("Attacking...%s took %s damage due to a 5x multiplier from the %s" % (self._name, damage, weapon.getWeaponType()))
			else:
				self._HP -= damage
				print("Attacking...%s took %s damage" % (self._name, damage))
			
			if self._HP <= 0:
				print("A ghould has died!")
				self.update_observable(self)
				self.clear_observers()
				
"""
The Werewolf NPC that is to be used in the Zork game.
Is a sublcass of the NPC class.
"""
class Werewolf(NPC):
	"""
	Initial constructor of the Person class. 
	Calls the superclasses constructor.
	"""
	def __init__(self):
		NPC.__init__(self, "Werewolf", 200, 0, 40)

	"""
	Implementation of the takeDamage() method found in the NPC superclass.
	Calculates and applies damage to the NPC based on the attack done to it.
	Updates the house observer if the monster dies.

	@param damage - int - the base damage done to the Werewolf
	@param weapon - str - the weapon used to attack the Werewolf
	"""
	def takeDamage(self, damage, weapon):
	 	if weapon.getWeaponType() == 'Chocolate Bar':
	 		print("Attacking...the %s seems to actually enjoy the %s -_-" % (self._name, weapon.getWeaponType()))
	 	elif weapon.getWeaponType() == 'Sour Straw':
	 		print("Attacking...the %s seems to actually enjoy the %s -_-" % (self._name, weapon.getWeaponType()))
	 	else:
	 		self._HP -= damage
	 		print("Attacking...%s took %s damage" % (self._name, damage))
	 	if self._HP <= 0:
	 		print("A werewolf has died!")
	 		self.update_observable(self)
	 		self.clear_observers()