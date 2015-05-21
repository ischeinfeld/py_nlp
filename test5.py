from decoder_class import Decoder

sentence = "The man jumped across the track, breaking his leg."

decoder = Decoder("train")

decode = decoder.decode(sentence)

print(decode[0])
print(decode[1])
