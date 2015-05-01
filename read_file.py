develop = "/Users/ischeinfeld/Documents/Code/WSJ/develop.txt"

with open(develop, "r") as infile:
	for line in infile:
		print line
		print '*'