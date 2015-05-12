from preprocessing import import_wsj, replace_rarities
from parameters import sx_counts, uvs_counts, uv_counts, s_counts

sentences = import_wsj("train")
#print(sentences[0])

new_sentences = replace_rarities(sentences)
#print(new_sentences[0])

sx_counts = sx_counts(new_sentences)
uvs_counts = uvs_counts(new_sentences)
s_counts = s_counts(new_sentences)
uv_counts = uv_counts(new_sentences)

num_tags = 0
for key in sx_counts:
	num_tags += 1

print()
print("There are " + str(num_tags) + " tags.")

print()
print("c(s,x) -> c(DT, the): ", sx_counts['DT']['the'])

print()
print("c(u,v,s) -> c(<!>, NN, NNS): ", uvs_counts['<!>']['NN']['NNS'])

print()
print("c(s) -> c(DT): ", s_counts['DT'])

print()
print("c(u,v) -> c(<!>, NN): ", uv_counts['<!>']['NN'])

print()