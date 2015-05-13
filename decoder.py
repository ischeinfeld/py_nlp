"""Decodes a sentence using the Viterbi Algorithm

Input: a sentence (str), parameters q(s|u,v) and e(x|s)
Initialization: set pi(0, <START>, <START>) = 1

"""

from preprocessing import import_wsj, replace_rarities
from parameters import sx_counts, uvs_counts, uv_counts, s_counts, q, e