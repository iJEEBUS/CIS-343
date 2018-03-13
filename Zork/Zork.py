from House import House
from Monster import Monster
from Weapon import Weapon
from Player import Player
from Neighborhood import Neighborhood

def promptForPlayStyle():
	try:
		print("\nWhich type of experience would you prefer?")
		print("1) Automated")
		print("2) Manual")	
		return play_style
	except Exception as e:
		getPlayStyle()

def promptForRows():
	try:
		rows = int(input("How many rows of houses are in your neighborhood? "))
		return rows
	except Exception as e:
		get_rows_from_user()
	

def promptForCols():
	try:
		cols = int(input("Now, how many columns of houses are there? "))
		return cols
	except Exception as e:
		get_cols_from_user()


if __name__ == "__main__":

	print("\nzorKK")

	play_style = promptForPlayStyle()
	print('\n')
	rows = promptForRows()
	cols = promptForCols()
	print("\n")

	# create neighborhood instance
	n = Neighborhood(rows,cols)
	n.showNeighborhood()

	# create a player instance
	p = Player()
	inventory = p.getInventory()


	# travel from house to house, fighting monsters