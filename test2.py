"""Tests that q and e sum to 1 or 0"""

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


## Test q

print()
print("TESTING q(s|u,v)")
print()

tags = []
for key in s_counts:
	tags.append(key)
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

print("If nothing but 0s appears above, \
than all is good with q(s|u,v).")


## Test e

print()
print("TESTING e(x|s)")
print()

should_be_ones = []
for s in sx_counts:
	sum = 0
	for x in sx_counts[s]:
		#print("for ", x, " in ", s)
		sum += e(sx_counts, s_counts, x, s)
	should_be_ones.append([s, sum])
	
for double in should_be_ones:
	if not .9999 < double[1] < 1.0001:
		print(double)
		
print("If nothing appears above, than all is good with e(x|s).")