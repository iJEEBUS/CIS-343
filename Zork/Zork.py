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
		self.__playGame()

	def update_observer(self, obj):
		print("%s has been transformed into a human again!" % (obj.getName()))
		if self.__isHouseEmpty():
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

	def __playGame(self):
		print("\x1b[37m")
		print("\nzorKK")
		print('\n')
		rows = self.promptForRows()
		cols = self.promptForCols()
		print("\n")

		# create neighborhood instance
		self.__neighborhood = Neighborhood(rows, cols)
		self.__neighborhood.showNeighborhood()

		user_input = ""
		while user_input not in ['exit','quit']:
			user_input = ""
			user_input = input("Enter a command: ").lower()
			print('\n')

			if user_input in ['nuke', 'bomb']:
				self.__neighborhood.nuke()
				quit()

			if user_input in ['list', 'weapons']:
				self.__player.listInventory()

			if user_input in ['0','1','2','3','4','5','6','7','8','9']:
				self.__player.setCurrentWeapon(int(user_input))
				self.__neighborhood.showNeighborhood()
				print("Current weapon set to %s - %s remaining" % (self.__player.getCurrentWeapon().getWeaponType(), self.__player.getCurrentWeapon().getUsesLeft()))

			if user_input == "map":
				self.__neighborhood.showNeighborhood()

			if user_input in ["stats", "statistics"]:
				self.__player.showPlayerStatistics()
				self.__neighborhood.showNeighborhoodStatistics()

			if user_input == "attack": ## attack
				if self.__isHouseEmpty() == False:
					print("Attacking with a %s" % (self.__player.getCurrentWeapon().getWeaponType()))
					house = self.__neighborhood.getNeighborhood()[self.__current_row][self.__current_col].getNPCs()
					for monster in house:
						print("Attacking %s...", (monster))

					self.__player.attackWithWeapon(self.__player.getCurrentWeapon())
					self.__player.getCurrentWeapon().decrementUsesLeft()

			if user_input == 'w': # up
				pass

			if user_input == 's': # down
				pass
					


			if user_input == 'a': # left
				pass
					


			if user_input == 'd': # right
				pass
					
			else:
				pass
				
				
	def __isHouseEmpty(self):
		if self.__neighborhood.getNumMonstersSpecificHouse(self.__current_row, self.__current_col):
			return False
		else:
			return True


	def promptForPlayStyle(self):
		try:
			print("\nWhich type of experience would you prefer?")
			print("1) Automated")
			print("2) Manual")
			play_style = int(input(""))
			if play_style not in [1,2]:
				self.promptForPlayStyle()
			return play_style
		except Exception as e:
			self.promptForPlayStyle()

Zork(5,5)