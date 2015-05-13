"""Tests the functionality of parameters_class"""

from preprocessing import import_wsj
from parameters_class import Parameters

sentences = import_wsj("train")

params = Parameters(sentences)

print(params.q("NN", "DT", "NN"))
