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

num_tags = 0
for key in sx_counts:
	num_tags += 1

print()
print("There are " + str(num_tags) + " tags.")

print()
print("c(s,x) -> c(DT, the): ", sx_counts['DT']['the'])

print()
print("c(u,v,s) -> c(<START>, NN, NNS): ", uvs_counts['<START>']['NN']['NNS'])

print()
print("c(s) -> c(DT): ", s_counts['DT'])

print()
print("c(u,v) -> c(<START>, NN): ", uv_counts['<START>']['NN'])

print()
print()

q_suv = q(uvs_counts, uv_counts, "NNS", "<START>", "NN")
e_xs = e(sx_counts, s_counts, "the", "DT")

print("q(s|u,v) -> q(NNS, <START>, NN): ", q_suv)
print()

print("e(x|s) -> e(the, DT): ", e_xs)
print()