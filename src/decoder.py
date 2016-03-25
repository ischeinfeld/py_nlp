"""Decodes a sentence using the Viterbi Algorithm

Input: a sentence (str)
Initialization: set pi(0, <START>, <START>) = 1

"""

from math import log, exp
from nltk.tokenize import TreebankWordTokenizer

from src.preprocessing import import_wsj
from src.parameters import Parameters

class Decoder:

	def __init__(self, corpus_name, rarity=5):
		"""Initialize parameters using a corpus

		Parameters q (transition) and e (emission) are calculated by eponymous
		functions from the class Parameters using counts over the corpus.
		See parameters_class.py for details.

		The corpus must be from the Penn WSJ treebank

		corpus_name can be one of three names:
			"train" uses /Users/ischeinfeld/Documents/Code/WSJ/train.txt
			"develop" uses /Users/ischeinfeld/Documents/Code/WSJ/develop.txt"
			"test" uses /Users/ischeinfeld/Documents/Code/WSJ/test.txt"

		or corpus_name can be a complete path to the corpus text:
			ex. /dir/dir/dir/file(.txt)
		"""

		### Create instance of Parameters with the given corpus
		# Note that this completes all the counts for q and e

		self.corpus = import_wsj(corpus_name)
		self.params = Parameters(self.corpus)


	def decode(self, sentence):
		"""Decode a sentence

		Input: a sentence (str)

		Output: a tuple with lists of tokens and tags
		"""

		if isinstance(sentence, str):
			token_seq = self.prep_sentence(sentence) # Tokenize sentence
			#print("decoder_class_log, token_seq from string", token_seq)
		else:
			token_seq = sentence[0] # Already tokenized
			#print("decoder_class_log, token_seq from list", token_seq)

		for i in range(len(token_seq)):          # Replace rare words
			token_seq[i] = self.params.rep_rare_input(token_seq[i])


		print("Token sequence after replacing rarities:", token_seq)

		### Calculate pi values (log probabilities) and store back pointers

		pi = []
		bp = []
		tags = self.params.tags

		pi.append({})
		pi[0]['<START>'] = {}
		pi[0]['<START>']['<START>'] = 0 # pi[k][u][v] = 0 because log1 = 0

		bp.append({})
		bp[0]['<START>'] = {}
		bp[0]['<START>']['<START>'] = None # pi[k][u][v]

		for k in range(1, len(token_seq) + 1):
			pi.append({}) # pi[k] = {}
			bp.append({}) # bp[k] = {}
			for u in tags:
				pi[k][u] = {}
				bp[k][u] = {}
				for v in tags:
					max = float('-inf')
					pi[k][u][v] = max # Pi value
					bp[k][u][v] = None # back pointer value
					for w in pi[k-1].keys():
						try:
							print("marker")
							log_prob = (pi[k-1][w][u] + log(self.params.q(v, w, u))
									+ log(self.params.e(token_seq[k - 1],v)))
									# token_seq[k-1] is the token at v
						except KeyError:
							log_prob = float('-inf')
						except ValueError:
							log_prob = float('-inf')

						if log_prob >= max: # Explicit
							max = log_prob
							pi[k][u][v] = log_prob # New max log probability
							bp[k][u][v] = w # Backpointer to w

		### Find last two tags, using <STOP> transition probability

		max = float('-inf')
		for u in tags:
			for v in tags:
				try:
					log_prob = (pi[len(token_seq)][u][v]
								+ log(self.params.q('<STOP>', u, v)))
				except KeyError:
					log_prob = float('-inf')
				except ValueError:
					log_prob = float('-inf')

				if log_prob >= max: # Explicit
					max = log_prob
					yn, yn_1 = v, u #  | yn is y sub n |  yn_1 is y sub (n-1)

		### Get tag sequence using backtracking

		tag_seq = [] # Replace with ['<START>', '<START>'] if desired
		for word in token_seq:
			tag_seq.append(None)

		tag_seq[-1] = yn
		tag_seq[-2] = yn_1

		for i in range(len(tag_seq) - 3, -1, -1):
			tag_seq[i] = bp[i+3][tag_seq[i+1]][tag_seq[i+2]]

		print("Log probability is:", max)
		print("Probability is:", exp(max))
		return (token_seq, tag_seq)

	def prep_sentence(self, sentence):
		"""Tokenizes a sentence string"""
		sentence_list = TreebankWordTokenizer().tokenize(sentence)
		return sentence_list
