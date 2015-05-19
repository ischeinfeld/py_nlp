"""Decodes a sentence using the Viterbi Algorithm

Input: a sentence (str)
Initialization: set pi(0, <START>, <START>) = 1

"""

from nltk.tokenize import TreebankWordTokenizer

from preprocessing import import_wsj
from parameters_class import Parameters

class Decoder:

	def __init__(self, corpus_name):
		"""Initialize parameters using a corpus

		The corpus must be from the Penn WSJ treebank

		corpus_name can be one of three names:
			"train" uses /Users/ischeinfeld/Documents/Code/WSJ/train.txt
			"develop" uses /Users/ischeinfeld/Documents/Code/WSJ/develop.txt"
			"test" uses /Users/ischeinfeld/Documents/Code/WSJ/test.txt"

		or corpus_name can be a complete path to the corpus text:
			ex. /dir/dir/dir/file(.txt)
		"""

		self.corpus = import_wsj(corpus_name)
		self.params = Parameters(self.corpus)


	def decode(self, sentence):
		"""Decode a sentence

		Input: a sentence (str)

		Output: a tuple with lists of tokens, tags, and probabilities
		"""

		token_seq = self.prep_sentence(sentence)

		### Calculate pi values

		pi = []
		tags = self.params.tags

		pi[0] = {'<START>': {'<START>': 0}} # pi[k][u][v]

		for k in range(1, len(token_seq)):
			for w in pi[k-1]:
				for u in pi[k-1][w]:
					for v in tags:
						pi[k][u][v] = pi[k-1][w][u] * self.params.q(v, w, u) * self.params.e(token_seq[i],v)

		'''
		tag_seq = ['<START>', '<START>']
		prob_seq = []

		return (token_seq, tag_seq, prob_seq)
		'''

		for k in pi:
			for u in pi[k]:
				for v in pi[k][u]:
					print("pi(", k, ", ", u, ", ", v, ")")

	def get_prob(self, u, v, s, x):

		q = self.params.q(s, u, v)

		e = self.params.e(x, s)

		return q * e


	def prep_sentence(self, sentence):
		"""Tokenizes a sentence string"""
		sentence_list = TreebankWordTokenizer().tokenize(sentence)
		return sentence_list
