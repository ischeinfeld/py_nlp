from decoder_class_log import Decoder

sentence = "Today is most often used as a noun."

decoder = Decoder("train", 5)

decode = decoder.decode(sentence)

print(list(zip(decode[0],decode[1])))
