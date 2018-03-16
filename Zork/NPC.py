from Observable import Observable
from random import randint

class NPC(Observable):
	def __init__(self, name, HP, min_attack, max_attack):
		super(NPC, self).__init__()
		self.__name = name
		self.__HP = HP
		self.__min_attack = min_attack
		self.__max_attack = max_attack

		def takeDamage(self, damage, weapon):
			raise NotImplementedError
		def attack(self):
			return randint(self.__min_attack, self.__max_attack)
		def getName(self):
			return self.__name
		def __checkIfAlive(self):
			if self.__HP <= 0:
				self.update_observable() # updates the house on the death
				self.remove_observers() # removes everything watching this character

class Player(NPC):
	def __init__(self):
		NPC.__init__(self, "Person", 100, 0, 0)

	def takeDamage(self, damage, weapon):
		pass
	def attack(self):
		return -3 # since a negative attack will increase the players health

class Zombie(NPC):
	def __init__(self, arg):
		NPC.__init__(self, "Zombie", randint(50, 100), 0, 10)

	def takeDamage(self, damage, weapon):
		# Check weapon type and modify damage when needed
		if weapon == "Sour Straw":
			damage *=2
			self.__HP -= damage
			print("%s took %s damage due to a 2x multiplier from the %s" % (self.__name, damage, weapon))
		else:
			self.__HP -= damage
			print("%s took %s damage" % (self.__name, damage))
		self.__checkIfAlive() # removes any observers if the NPC dies

class Vampire(NPC):
	def __init__(self):
		NPC.__init__(self, "Vampire", randint(100, 200), 10, 20)
		
	def takeDamage(self, damage, weapon):
		if weapon != "Chocolate Bar":
			self.__HP -= damage
			print("%s took %s damage" % (self.__name, damage))
			self.__checkIfAlive()
		else:
			print("The %s seems to actually enjoy the %s -_-" % (self.__name, weapon))

class Ghoul(NPC):
	def __init__(self):
		NPC.__init__(self, "Ghoul", randint(40, 80), 15, 30)

	def takeDamage(self, damage, weapon):
		if weapon == "Nerd Bomb":
			damage *= 5
			self.__HP -= damage
			print("%s took %s damage due to a 5x multiplier from the %s" % (self.__name, damage, weapon))
		else:
			self.__HP -= damage
			print("%s took %s damage" % (self.__name, damage))
		self.__checkIfAlive()

class Werewolf(NPC):
	def __init__(self):
		NPC.__init__(self, "Werewolf", 200, 0, 40)

	def takeDamage(self, damage, weapon):
	 	if weapon == 'Chocolate Bar':
	 		print("The %s seems to actually enjoy the %s -_-" % (self.__name, weapon))
	 	if weapon == 'Sour Straw':
	 		print("The %s seems to actually enjoy the %s -_-" % (self.__name, weapon))
	 	else:
	 		self.__HP -= damage
	 		print("%s took %s damage" % (self.__name, damage))
	 		self.__checkIfAlive()
		
		
		

		


