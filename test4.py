from decoder_class import Decoder

sentence = "The man could not understand him."

decoder = Decoder("train")

decode = decoder.decode(sentence)

print(decode)