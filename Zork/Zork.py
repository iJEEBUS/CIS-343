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
		print("========================================================= zorKK! =========================================================")
		print("It seemed like a normal Halloween Eve.")
		print("You bought a lot of candy, ate a lot of candy, and went to bed early.")
		print("You had a lot trick-or-treating to do the next day.\n")
		print("Unfortunately, when you woke up you discovered that the world was not how you left it.")
		print("Batches of bad candy had transformed your friends and neighbors into all sorts of crazy monsters.")
		print("Somehow you missed the tainted candy; it is therefore up to you to save your neighborhood and turn everyone back to normal.")
		print("\n\n========================================================= Manual =========================================================")
		print("* = player location")
		print("#'s show how many monsters are in each house")
		print("W - up, S - down, A - left, D - right")
		print("Enter 'exit' or 'quit' to exit the game...enjoy!\n")

	def automateGame(self):
		self.n.showNeighborhood()





	def playGame(self):
		self.printDirections()

		user_input = ""
		while user_input not in ['exit','quit']:
			user_input = ""
			self.n.showNeighborhood()
			user_input = input("Enter a command: ").lower()
			print("\nPlayer coordinates: %s, %s\n" % (self.p.getLocationX(), self.p.getLocationY()))

			if user_input in ['nuke', 'bomb']:
				self.n.nuke()
				quit()

			if user_input == 'w':
				if (self.p.getLocationY()-1) >= 0:
					self.n.update(0, -1)
					self.p.setLocationY(self.p.getLocationY()-1)

					## Implement fighting logic


			if user_input == 's':
				if (self.p.getLocationY()+1) <= self.rows:
					self.n.update(0, 1)
					self.p.setLocationY(self.p.getLocationY()+1)

					## Implement fighting logic


			if user_input == 'a':
				if (self.p.getLocationX()-1) >= 0:
					self.n.update(-1,0)
					self.p.setLocationX(self.p.getLocationX()-1)

					## Implement fighting logic


			if user_input == 'd':
				if (self.p.getLocationX()+1) <= self.cols:
					self.n.update(1,0)
					self.p.setLocationX(self.p.getLocationX()+1)

					## Implement fighting logic








	def game(self):
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

