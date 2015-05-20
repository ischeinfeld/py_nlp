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
		tag_seq = ['<START>', '<START>']

		### Calculate pi values and store back pointers

		pi = []
		bp = []
		tags = self.params.tags

		pi.append({})
		pi[0]['<START>'] = {}
		pi[0]['<START>']['<START>'] = 1 # pi[k][u][v]

		bp.append({})
		bp[0]['<START>'] = {}
		bp[0]['<START>']['<START>'] = None # pi[k][u][v]


		for k in range(1, len(token_seq)):
			pi.append({}) # pi[k] = {}
			bp.append({}) # bp[k] = {}
			for u in tags:
				pi[k][u] = {}
				bp[k][u] = {}
				for v in tags:
					max = 0.0
					pi[k][u][v] = max # Pi value
					bp[k][u][v] = None # back pointer value
					for w in pi[k-1].keys(): # for w that produces hightest prob u v, keep w (where?)
						try:
							prob = pi[k-1][w][u] * self.params.q(v, w, u) * self.params.e(token_seq[k - 1],v) # k-1 at end because token_seq is indexed from 0
						except KeyError:
							prob = 0.0
						if prob >= max:
							max = prob
							pi[k][u][v] = prob
							bp[k][u][v] = w

		for k in bp:
			print()
			print(k)
			print()

		'''
		return (token_seq, tag_seq, prob_seq)
		'''


	def get_prob(self, u, v, s, x):

		q = self.params.q(s, u, v)

		e = self.params.e(x, s)

		return q * e


	def prep_sentence(self, sentence):
		"""Tokenizes a sentence string"""
		sentence_list = TreebankWordTokenizer().tokenize(sentence)
		sentence_list.append('<STOP>')
		return sentence_list
