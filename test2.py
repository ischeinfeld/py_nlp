from preprocessing import import_wsj, replace_rarities
from parameters import sx_counts, uvs_counts, uv_counts, s_counts, q, e

sentences = import_wsj("train")
#print(sentences[0])

new_sentences = replace_rarities(sentences)
#print(new_sentences[0])

sx_counts = sx_counts(new_sentences)
uvs_counts = uvs_counts(new_sentences)
s_counts = s_counts(new_sentences)
uv_counts = uv_counts(new_sentences)

tags = []
for key in s_counts:
	tags.append(key) #TODO
tags.append("<START>") # <START> and <STOP> are not in s_counts
tags.append("<STOP>")
	
#print(tags)

should_be_ones = []
for u in tags:
    for v in tags:
        sum = 0
        for s in tags:
            sum += q(uvs_counts, uv_counts, s, u, v)
        should_be_ones.append([u,v,sum])
        
#print(should_be_ones)

for triple in should_be_ones:
	if not .9999 < triple[2] < 1.0001:
		print(triple)