import copy


def q(uvs_counts, uv_counts, s, u, v):
	""" q(s|u,v) """
	
	try:
		return uvs_counts[u][v][s] / uv_counts[u][v]
	except KeyError:
		return 0

def e(sx_counts, s_counts, x, s):
	""" e(x|s) """
	
	try:
		return sx_counts[s][x] / s_counts[s]
	except KeyError:
		return 0


def uv_counts(input_sentences):
	""" Sum c(u,v) """

	sentences = copy.deepcopy(input_sentences)

	for sentence_tags in sentences:
		sentence_tags[1].insert(0, "<START>") # Add buffer tags before tag sequence
		sentence_tags[1].insert(0, "<START>")
		sentence_tags[1].append("<STOP>") # Add stop symbol, Note, in uv_counts kept only for indexing


	q = {}

	for i in range(len(sentences)):
		for j in range(2, len(sentences[i][1])): # [1] is for tags, not same # words and tags

			u = sentences[i][1][j-2]
			v = sentences[i][1][j-1]

			if not u in q:
				q[u] = {}
			if not v in q[u]:
				q[u][v] = 0

			q[u][v] += 1
	return q


def s_counts(input_sentences):
	""" Sum c(s) """

	sentences = copy.deepcopy(input_sentences)

	e = {} # counts

	for i in range(len(sentences)):
		for j in range(len(sentences[i][0])): # [0] is for words, not same # words and tags
			s = sentences[i][1][j]

			if not s in e:
				e[s] = 0

			e[s] += 1

	return e

def uvs_counts(input_sentences):
	""" Sum c(u,v,s)
	
	if not u in q:
		q[u] = {}
		if not v in q[u]:
			q[u][v] = {}
			q[u][v][s] = ...
	"""

	sentences = copy.deepcopy(input_sentences)

	for sentence_tags in sentences:
		sentence_tags[1].insert(0, "<START>") # Add buffer tags before tag sequence
		sentence_tags[1].insert(0, "<START>")
		sentence_tags[1].append("<STOP>") # Add stop symbol


	q = {}

	for i in range(len(sentences)):
		for j in range(2, len(sentences[i][1])): # [1] is for tags, not same # words and tags

			u = sentences[i][1][j-2]
			v = sentences[i][1][j-1]
			s = sentences[i][1][j]

			if not u in q:
				q[u] = {}
			if not v in q[u]:
				q[u][v] = {}
			if not s in q[u][v]:
				q[u][v][s] = 0

			q[u][v][s] += 1
	return q


def sx_counts(input_sentences):
	""" Sum c(s,x)

	"""

	sentences = copy.deepcopy(input_sentences)

	e = {} # counts

	for i in range(len(sentences)):
		for j in range(len(sentences[i][0])): # [0] is for words, not same # words and tags
			x = sentences[i][0][j]
			s = sentences[i][1][j]

			if not s in e:
				e[s] = {}
			if not x in e[s]:
				e[s][x] = 0

			e[s][x] += 1

	return e
