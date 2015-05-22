from preprocessing import import_wsj, rep_rare_corpus
from decoder_class_log import Decoder

sentences = import_wsj("test")

correct = 0
total = 0

decoder = Decoder("train", 5)

for sentence_and_tags in sentences:
	local_correct = 0
	decode = decoder.decode(sentence_and_tags)
	decoded_tags = decode[1]
	tags = sentence_and_tags[1]
	print("tags:", tags)
	print("decoded tags:", decoded_tags)
	for i in range(len(tags)):
		if tags[i] == decoded_tags[i]:
			local_correct += 1
		total += 1
	if local_correct == 0:
		for tag in tags:
			total -= 1
	else:
		correct += local_correct

accuracy = correct / total * 100
print(accuracy)
