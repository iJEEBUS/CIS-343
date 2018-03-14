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
			promptForPlayStyle(self)

	def promptForRows(self):
		try:
			rows = int(input("How many rows of houses are in your neighborhood? "))
			return rows
		except Exception as e:
			self.get_rows_from_user()
		

	def promptForCols(self):
		try:
			cols = int(input("Now, how many columns of houses are there? "))
			return cols
		except Exception as e:
			self.get_cols_from_user()

	def automateGame(self):
		self.n.showNeighborhood()


	def game(self):
		print("\nzorKK")
		self.play_style = self.promptForPlayStyle()
		print('\n')
		self.rows = self.promptForRows()
		self.cols = self.promptForCols()
		print("\n")

		# create neighborhood instance
		self.n = Neighborhood(self.rows,self.cols)
		#n.showNeighborhood()

		# create a player instance
		self.p = Player()

		if self.play_style == 1:
			self.automateGame()

p = Zork()
p.game()

