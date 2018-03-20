from Observable import Observable # observed by a house
from random import randint

class NPC(Observable):
	def __init__(self, name, HP, min_attack, max_attack):
		super(NPC, self).__init__() # pass itself to the Observable class
		self._name = name
		self._HP = HP
		self.__min_attack = min_attack
		self.__max_attack = max_attack

		def takeDamage(self, damage, weapon):
			raise NotImplementedError
		def attack(self):
			return randint(self.__min_attack, self.__max_attack)
		def getName(self):
			return self.__name

class Person(NPC):
	def __init__(self):
		NPC.__init__(self, "Person", 100, 0, 0)

	def takeDamage(self, damage, weapon):
		pass
	def attack(self):
		return -3 # since a negative attack will increase the players health

class Zombie(NPC):
	def __init__(self):
		NPC.__init__(self, "Zombie", randint(50, 100), 0, 10)

	def takeDamage(self, damage, weapon):
		# Check weapon type and modify damage when needed
		if self._HP > 0:
			print("Attacking Zombie...")
			if weapon == "Sour Straw":
				damage *=2
				self._HP -= damage
				print("%s took %s damage due to a 2x multiplier from the %s" % (self._name, damage, weapon))
			else:
				self._HP -= damage
				print("%s took %s damage" % (self._name, damage))
			if self._HP <= 0: # removes any observers if the NPC dies
				print("Zombie has died!")
				self.show_observers()
				self.update_observable(self) # updates the house on the death
				self.clear_observers() # removes everything watching this character
		else:
			pass

class Vampire(NPC):
	def __init__(self):
		NPC.__init__(self, "Vampire", randint(100, 200), 10, 20)
		
	def takeDamage(self, damage, weapon):
		if weapon != "Chocolate Bar":
			self._HP -= damage
			print("%s took %s damage" % (self._name, damage))
			#self.__checkIfAlive()
		else:
			print("The %s seems to actually enjoy the %s -_-" % (self._name, weapon))

class Ghoul(NPC):
	def __init__(self):
		NPC.__init__(self, "Ghoul", randint(40, 80), 15, 30)

	def takeDamage(self, damage, weapon):
		if weapon == "Nerd Bomb":
			damage *= 5
			self._HP -= damage
			print("%s took %s damage due to a 5x multiplier from the %s" % (self._name, damage, weapon))
		else:
			self._HP -= damage
			print("%s took %s damage" % (self._name, damage))
		#self.__checkIfAlive()

class Werewolf(NPC):
	def __init__(self):
		NPC.__init__(self, "Werewolf", 200, 0, 40)

	def takeDamage(self, damage, weapon):
	 	if weapon == 'Chocolate Bar':
	 		print("The %s seems to actually enjoy the %s -_-" % (self._name, weapon))
	 	if weapon == 'Sour Straw':
	 		print("The %s seems to actually enjoy the %s -_-" % (self._name, weapon))
	 	else:
	 		self._HP -= damage
	 		print("%s took %s damage" % (self._name, damage))
	 		#self.__checkIfAlive()
		
		
		

		


