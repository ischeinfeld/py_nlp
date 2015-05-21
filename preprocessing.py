import copy

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

def rep_rare_corpus(input_sentences, rarity):

	sentences = copy.deepcopy(input_sentences)

	words = {}

	for sentence_w_tags in sentences:
		for word in sentence_w_tags[0]:
			if word in words:
				words[word] += 1
			else:
				words[word] = 1

	sentence_num = 0
	for sentence_w_tags in sentences:

		word_num = 0
		for word in sentence_w_tags[0]:
			if words[word] < rarity:
				sentences[sentence_num][0][word_num] = "<?>"

			word_num += 1
		sentence_num += 1

	return sentences

