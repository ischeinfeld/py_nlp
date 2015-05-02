develop = "/Users/ischeinfeld/Documents/Code/WSJ/develop.txt"

sentences = []

def get_sents(file):
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


sentences = get_sents(develop)
print(sentences[0])