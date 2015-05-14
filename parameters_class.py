import copy
from preprocessing import replace_rarities
#from parameters import sx_counts

class Parameters:
	
	def __init__(self, sentences):
		self.new_sentences = replace_rarities(sentences) # Replaces rare words

		self._sx_counts = self.sx_counts(self.new_sentences)
		self._uvs_counts = self.uvs_counts(self.new_sentences)
		self._s_counts = self.s_counts(self.new_sentences)
		self._uv_counts = self.uv_counts(self.new_sentences)
		
		self.tags = []
		for key in self._s_counts:
			self.tags.append(key)
		self.tags.append("<START>") # <START> and <STOP> are not in s_counts
		self.tags.append("<STOP>")
	
	def q(self, s, u, v):
		""" q(s|u,v) """
		
		try:
			return self._uvs_counts[u][v][s] / self._uv_counts[u][v]
		except KeyError:
			return 0


	def e(self, x, s):
		""" e(x|s) """

		try:
			return self._sx_counts[s][x] / self._s_counts[s]
		except KeyError:
			return 0

# Functions		


	def uv_counts(self, input_sentences):
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


	def s_counts(self, input_sentences):
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

	def uvs_counts(self, input_sentences):
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


	def sx_counts(self, input_sentences):
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
