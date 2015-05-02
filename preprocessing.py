def import_wsj(corpus):

	TRAIN = "/Users/ischeinfeld/Documents/Code/WSJ/train.txt"
	DEVELOP = "/Users/ischeinfeld/Documents/Code/WSJ/develop.txt"
	TEST = "/Users/ischeinfeld/Documents/Code/WSJ/test.txt"

	if corpus == "train":
		file = TRAIN
	elif corpus == "develop":
		file = DEVELOP
	elif corpus == "test":
		file = TEST
	else:
		file = corpus # If a name is not given, the input is interpreted as a path

	sentences = []

	with open(file, "r") as infile:
		for line in infile:
	
			sentence = line.split()
			words = []
			tags = []

			for i in range(len(sentence)):
				if i%2 == 0:
					words.append(sentence[i])
				else:
					tags.append(sentence[i])

			sentences.append((words, tags))
	return sentences