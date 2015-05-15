"""NOTE: this works, but is wrong.

Decodes a sentence using the Viterbi Algorithm

Input: a sentence (str)
Initialization: set pi(0, <START>, <START>) = 1

"""

from nltk.tokenize import TreebankWordTokenizer

from preprocessing import import_wsj
from parameters_class import Parameters

class Decoder:

	def __init__(self, corpus_name):
		"""Initialize parameters using named corpus"""
		self.corpus = import_wsj(corpus_name)
		self.params = Parameters(self.corpus)
		
	def decode(self, sentence):
		"""Decode a sentence
		
		returns a tuple with lists of tokens, tags, and probabilities
		probabilities are not cumulative
		"""
		tokens = self.prep_sentence(sentence)
		tags = ['<START>', '<START>']
		probs = []
		
		for i in range(len(tokens)):
			new_tag_prob = self.next_tag(i, tokens, tags, probs)
			tags.append(new_tag_prob[0])
			probs.append(new_tag_prob[1])
		
		probs.append(self.params.q('<STOP>', tags[-1], tags[-2])) # Adds final tag and its prob
		tags.append('<STOP>')
		
		return (tokens, tags, probs)
	
	
	def next_tag(self, i, tokens, tags, prev_probs):
		"""Returns the tag for a token and the latest probability
		
		Input: index, tokens, tags, probabilities
		"""
		probs = []
		
		for tag in self.params.tags:
			probs.append(self.get_prob(tags[i], tags[i+1], tag, tokens[i])) # (u, v, s, x)
			
		if all(prob == 0.0 for prob in probs): # True if token not in training data
			probs = []
			
			for tag in self.params.tags:
				probs.append(self.get_prob(tags[i], tags[i+1], tag, '<?>'))
			
		max_prob = max(probs)
		max_prob_index = probs.index(max_prob)
		
		return (self.params.tags[max_prob_index], max_prob)
		
	def get_prob(self, u, v, s, x):
		
		q = self.params.q(s, u, v)
		
		e = self.params.e(x, s)
			
		return q * e
		
	def prep_sentence(self, sentence):
		"""Tokenizes a sentence string"""
		sentence_list = TreebankWordTokenizer().tokenize(sentence)
		return sentence_list

		
		