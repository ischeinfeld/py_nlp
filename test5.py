from decoder_class import Decoder

sentence = "The man could not understandeder him."

decoder = Decoder("train")

decode = decoder.decode(sentence)

print(decode)