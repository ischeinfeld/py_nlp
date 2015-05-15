"""Tests the functionality of parameters_class"""

from preprocessing import import_wsj
from parameters_class import Parameters

sentences = import_wsj('train')

params = Parameters(sentences)

print("q(<STOP>|NN,.): ", params.q('<STOP>', 'NN', '.'))

print("e(the|DT): ", params.e("the", "DT"))

print("If the time between now ...")
params.q('NN', 'DT', 'NN')
params.q('NN', 'DT', 'NN')
params.q('NN', 'DT', 'NN')
params.q('NN', 'DT', 'NN')
params.q('NN', 'DT', 'NN')
print("... and now is not long, than the class is preserving counts.")