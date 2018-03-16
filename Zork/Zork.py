from House import House
from Monster import Monster
from Weapon import Weapon
from Player import Player
from Neighborhood import Neighborhood
class Zork(object):
	def __init__(self):
		super().__init__()

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

	def automateGame(self):
		self.n.showNeighborhood()





	def playGame(self):
		self.printDirections()
		self.n.showNeighborhood()
		self.p.showStatistics()

		user_input = ""
		while user_input not in ['exit','quit']:
			user_input = ""
			user_input = input("Enter a command: ").lower()
			print('\n')

			if user_input in ['nuke', 'bomb']:
				self.n.nuke()
				quit()

			if user_input in ['list', 'weapons']:
				self.p.listInventory()

			if user_input in ['0','1','2','3','4','5','6','7','8','9']:
				self.p.setCurrentWeapon(int(user_input))
				self.n.showNeighborhood()
				self.p.showStatistics()

			if user_input == "map":
				self.n.showNeighborhood()

			if user_input in ["stats", "statistics"]:
				self.p.showStatistics()

			if user_input == 'w':
				if (self.p.getLocationY()-1) >= 0:
					self.n.update(0, -1)
					self.p.setLocationY(self.p.getLocationY()-1)
				self.n.showNeighborhood()
				self.p.showStatistics()

					## Implement fighting logic


			if user_input == 's':
				if (self.p.getLocationY()+1) < self.rows:
					self.n.update(0, 1)
					self.p.setLocationY(self.p.getLocationY()+1)
				self.n.showNeighborhood()
				self.p.showStatistics()

					## Implement fighting logic


			if user_input == 'a':
				if (self.p.getLocationX()-1) >= 0:
					self.n.update(-1,0)
					self.p.setLocationX(self.p.getLocationX()-1)
				self.n.showNeighborhood()
				self.p.showStatistics()

					## Implement fighting logic


			if user_input == 'd':
				if (self.p.getLocationX()+1) < self.cols:
					self.n.update(1,0)
					self.p.setLocationX(self.p.getLocationX()+1)
				self.n.showNeighborhood()
				self.p.showStatistics()

					## Implement fighting logic
			else:
				self.n.showNeighborhood()
				self.p.showStatistics()









	def game(self):
		print("\x1b[37m")
		print("\nzorKK")
		self.play_style = self.promptForPlayStyle()
		print('\n')
		self.rows = self.promptForRows()
		self.cols = self.promptForCols()
		print("\n")



		# create a player instance
		self.p = Player()
		# create neighborhood instance
		self.n = Neighborhood(self.rows,self.cols, self.p)
		#n.showNeighborhood()

		if self.play_style == 1:
			self.automateGame()
		if self.play_style == 2:
			self.playGame()

p = Zork()
p.game()