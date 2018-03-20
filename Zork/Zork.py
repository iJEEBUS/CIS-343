from Observer import Observer
from Player import Player
from Neighborhood import Neighborhood

class Zork(Observer):
	def __init__(self, max_columns, max_rows):
		self.__max_column = max_columns
		self.__max_row = max_rows
		self.__current_col = 0
		self.__current_row = 0
		self.__neighborhood = Neighborhood(max_columns, max_rows)
		self.__neighborhood.add_observer(self)
		self.__player = Player()
		self.__playGame(self.__max_column, self.__max_row)


	def playAgain(self):
		response = input("Would you like to play again? ").lower()
		if response == "yes":
			Zork(5,5)
		else:
			print("LOL loser")
			quit()

	def update_observer(self, obj):
		print("%s has been transformed into a human again!" % (obj.getName()))
		if self.__containsMonsters() == False:
			print("You have defeated all of the monsters at this house!")
			print("The survivors provide you with more candy, which boosts your health: +10 HP")
			self.__player.takeDamage(-10) # negatively taking damage == adding health

	def promptForRows(self):
		try:
			rows = int(input("How many rows of houses are in your neighborhood? "))
			return rows
		except Exception as e:
			self.promptForRows()


	def promptForCols(self):
		try:
			cols = int(input("Now, how many columns of houses are there? "))
			return cols
		except Exception as e:
			self.promptForCols()

	def printDirections(self):
		print("\n\n\n\n========================================================= zorKK! =========================================================")
		print("It seemed like a normal Halloween Eve.")
		print("You bought a lot of candy, ate a lot of candy, and went to bed early.")
		print("You had a lot trick-or-treating to do the next day.\n")
		print("Unfortunately, when you woke up you discovered that the world was not how you left it.")
		print("Batches of bad candy had transformed your friends and neighbors into all sorts of crazy monsters.")
		print("Somehow you missed the tainted candy; it is therefore up to you to save your neighborhood and turn everyone back to normal.")
		print("\n\n========================================================= Manual =========================================================")
		print("\u2588 = player location")
		print("#'s -> how many monsters are in each house")
		print("W -> up")
		print("S -> down")
		print("A -> left")
		print("D -> right")
		print("list -> show all weapons")
		print("map -> show the map of the neighborhood")
		print("stats -> display player statistics")
		print("\'exit\' or \'quit\' -> exit game\n\n\n\n")

	def __playGame(self, max_columns, max_rows):
		print("\x1b[37m")
		print("\nzorKK")
		print('\n')
		rows = max_rows#self.promptForRows()
		cols = max_columns#self.promptForCols()
		print("\n")

		# create neighborhood instance
		self.__neighborhood = Neighborhood(rows, cols)
		#self.__neighborhood.showNeighborhood(self.__current_row, self.__current_col)

		user_input = ""

		# only exits when the user types 'exit' or 'quit'
		while user_input not in ['exit','quit'] :
			self.__neighborhood.showNeighborhood(self.__current_row, self.__current_col)
			print('\n')

			self.__player.showPlayerStatistics()
			print("Monsters remaining: %s" % (self.__neighborhood.getTotalMonsters()))
			user_input = ""
			user_input = input("Enter a command: ").lower()
			print('\n')

			# Just for giggles
			if user_input in ['nuke', 'bomb']:
				self.__neighborhood.nuke()
				quit()

			# Lists the players current inventory
			if user_input in ['list', 'weapons']:
				self.__player.listInventory()


			# Sets the weapon to the inputted number
			if user_input in ['0','1','2','3','4','5','6','7','8','9']:
				self.__player.setCurrentWeapon(int(user_input))
				self.__neighborhood.showNeighborhood(self.__current_row, self.__current_col)
				print("Current weapon set to %s - %s remaining" % (self.__player.getCurrentWeapon().getWeaponType(), self.__player.getCurrentWeapon().getUsesLeft()))

			# displays the map for the use
			#if user_input == "map":
			#	self.__neighborhood.showNeighborhood(self.__current_row, self.__current_col)
			#	print('\n')


			# THIS IS EXTRA
			#
			# display user health and number of monsters remaining
			#
			# THIS IS EXTRA
			if user_input in ["stats", "statistics"]:
				self.__player.showPlayerStatistics()
				self.__neighborhood.showNeighborhoodStatistics()


			# when a user wishes to attack the current house
			if user_input == "attack": ## attack

				weapon = self.__player.getCurrentWeapon()

				# if the house contains monsters then continue with attack
				if self.__containsMonsters():

					# if the weapon has uses left then continue attacking
					if weapon.getUsesLeft() > 0:

						print("Attacking with a %s\n" % (self.__player.getCurrentWeapon().getWeaponType()))

						house = self.__neighborhood.getNeighborhood()[self.__current_row][self.__current_col].getNPCs()

						# How much damage is going to be done
						damage = self.__player.attackWithWeapon(self.__player.getCurrentWeapon())
						self.__neighborhood.attackHouse(self.__current_row, self.__current_col, damage, weapon)

						# enemies attack right after you attack
						monster_attack = self.__neighborhood.getNeighborhood()[self.__current_row][self.__current_col].attackPlayer()
						self.__player.takeDamage(monster_attack)

						# if the players health decreases to 0 
						# then display ending message and ask user 
						# if they wish to play again
						if self.__player.getHP() <= 0:
							print("You have fought valiantly, but you have failed your quest to save your family and friends. Shame.")
							self.playAgain()

						# checks if there are any more monsters alive
						if self.__neighborhood.getTotalMonsters() <= 0:
							print("You have won the game! Congrats!")
							self.playAgain()



					else:
						print("You do not have any more %ss left!" % (str(weapon)[str(weapon).index(".")+1:str(weapon).index(" ")]))
				else:
					print("This house contains no monsters!")

			# Controls the users movement throughout the game
			if user_input == 'd': # right
				if self.__current_col + 1 <= self.__max_column - 1:
					self.__current_col += 1
					#self.__neighborhood.showNeighborhood(self.__current_row, self.__current_col)
				else:
					print("You cannot escape your own neighborhood!! Turn around and save your friends!\n")

			if user_input == 'a': # left
				if self.__current_col - 1 >= 0:
					self.__current_col -= 1
					#self.__neighborhood.showNeighborhood(self.__current_row, self.__current_col)
				else:
					print("You cannot escape your own neighborhood!! Turn around and save your friends!\n")

			if user_input == 'w': # up
				if self.__current_row - 1 >= 0:
					self.__current_row -= 1
					#self.__neighborhood.showNeighborhood(self.__current_row, self.__current_col)
				else:
					print("You cannot escape your own neighborhood!! Turn around and save your friends!\n")

			if user_input == 's': # down
				if self.__current_row + 1 <= self.__max_row - 1:
					self.__current_row += 1
					#self.__neighborhood.showNeighborhood(self.__current_row, self.__current_col)
				else:
					print("You cannot escape your own neighborhood!! Turn around and save your friends!\n")

			# see how many monsters are alive on the board
			# if it is zero then display win screen and exit
			#if self.__neighborhood.getNumMonsters() == 0:
			#	print("You have cleared the entire neighborhood!")
				
				
	def __containsMonsters(self):
		if self.__neighborhood.getNumMonstersSpecificHouse(self.__current_row, self.__current_col) > 0:
			return True
		else:
			return False

Zork(5,5)